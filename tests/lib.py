from spacy.language import Language
from kg_detective import KG
from spacy import displacy
from pathlib import Path
import json
import csv

@Language.factory("kg", default_config={"labels": [], "rules": []})
def create_kg(nlp: Language, name: str, labels: list, rules: list):
  return KG(nlp, labels=labels, rules=rules)
  

def print_kg(doc):
  content = doc._.kg.items()
  for k, v in content:
    print("{} {} {}".format("="*6, k, "="*6))
    for t in v:
      print(t)

def print_doc(doc):
  for t in doc:
    print("{} {} {} {} {}".format(t.text, t.tag_, t.pos_, t.dep_, t.lemma_))

def graph(doc):
  svg = displacy.render(doc, style="dep", jupyter=False)
  file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
  output_path = Path("en_images/" + file_name)
  output_path.open("w", encoding="utf-8").write(svg)

def display(sentences, nlp):
  docs = []
  for s in sentences:
    #doc = nlp(s)
    #docs.append(doc)
    #print("*"*10)
    print(s)
    #print_kg(doc)
    #print_doc(doc)
    #print("*"*10)
    #graph(doc)


def _write_to_csv(fields, content, csvfile="review.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, encoding="utf8", mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)


def write2csv(sentences, nlp, rules):
  content = {}
  for r in rules:
    content[r] = []

  for s in sentences:
    doc = nlp(s)
    for r in rules:
      info = {
        "sentence": doc.text,
        r: json.dumps([t.text for t in doc._.kg[r]])
      }
      content[r].append(info)
  # write to multiple files
  for k, v in content.items():
    _write_to_csv(["sentence", k], v, csvfile="tbr/"+k+".csv")
    


