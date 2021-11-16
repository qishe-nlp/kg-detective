import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
import json
from importlib import import_module
import os.path, pkgutil


lang = "es"
pkg = PKG_INDICES[lang]

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
    write_to_csv(["sentence", k], v, csvfile="tbr/{}/kg_{}.csv".format(lang, k))

def test_kg_tbr_gen():
  #sentences = read_json('./S0405.json')
  data = get_lang_sens(lang) 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  rules = nlp.get_pipe("kg").rules
  sentences = sum([sens for _, sens in data.items()], [])
  sen_kg(sentences, nlp, rules)

