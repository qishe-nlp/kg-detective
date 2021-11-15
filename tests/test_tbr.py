import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
import json
from importlib import import_module
import os.path, pkgutil


lang = "de"
pkg = PKG_INDICES[lang]

def _add_bracket(ex):
  return "(" + ex + ")" if ex!=None else ""

def sen_structure(sentences, nlp):
  content = []
  for s in sentences:
    doc = nlp(s)
    structure_with_explanation = trs(doc, doc._.structure, lang)
    analysis = " ".join([t["text"] + _add_bracket(t["explanation"]) for t in structure_with_explanation])
    _data = {
      "sentence": s,
      "analysis": analysis,
      "tbr": analysis,
    }
    content.append(_data) 
  return content

def test_structure_tbr_gen():
  data = get_lang_sens(lang) 
  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')

  for name, sentences in data.items():
    content = sen_structure(sentences, nlp) 
    write_to_csv(["sentence", "analysis", "tbr"], content, csvfile="tbr/structure_"+name+".csv")

def sen_kg(sentences, nlp, rules):
  content = {}
  for r in rules:
    content[r] = []

  for s in sentences:
    doc = nlp(s)
    for r in rules:
      info = {
        "sentence": doc.text,
        r: json.dumps([t for t in doc._.kg[r]])
      }
      content[r].append(info)
  # write to multiple files
  for k, v in content.items():
    write_to_csv(["sentence", k], v, csvfile="tbr/kg_"+k+".csv")

def test_kg_tbr_gen():
  #sentences = read_json('./S0405.json')
  data = get_lang_sens(lang) 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  rules = nlp.get_pipe("kg").rules
  sentences = sum([sens for _, sens in data.items()], [])
  sen_kg(sentences, nlp, rules)

