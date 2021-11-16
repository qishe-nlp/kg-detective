from spacy.language import Language
from kg_detective import KG
from spacy import displacy
from pathlib import Path
import json
import csv
from importlib import import_module
import os.path, pkgutil


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
    print("{} {} {} {} {} {}".format(t.text, t.pos_, t.dep_, t.tag_, t.morph, t.lemma_))

def graph(doc, lang):
  svg = displacy.render(doc, style="dep", jupyter=False)
  file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
  output_path = Path(lang+ "_images/" + file_name)
  output_path.open("w", encoding="utf-8").write(svg)

def display(sentences, nlp):
  for s in sentences:
    doc = nlp(s)
    print("*"*10)
    print(s)
    #print_structure(doc)
    print_kg(doc)
    print_doc(doc)
    print("*"*10)
    graph(doc, nlp.meta["lang"])


def write_to_csv(fields, content, csvfile="review.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, encoding="utf8", mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)

def read_json(filename):
  data = []
  with open(filename) as f:
    data = json.load(f)
  return data


def get_lang_sens(lang):
  _pkg = import_module('tests.test_{}'.format(lang))
  _pkgpath = os.path.dirname(_pkg.__file__)
  data = {}
  for _, name, _ in pkgutil.iter_modules([_pkgpath]):
    if name != "test_"+lang:
      test_module = import_module('tests.test_{}.{}'.format(lang, name))    
      data[name] = getattr(test_module, '_sentences')
  return data


def write_to_json(filename, content):
  with open(filename, 'w') as outfile:
    json.dump(content, outfile)

