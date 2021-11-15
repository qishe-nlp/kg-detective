import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
import json
from importlib import import_module
import os.path, pkgutil


lang = "en"
pkg = PKG_INDICES[lang]

def explain(kg):
  d = {}
  for k, v in kg.items():
    d[kg_en_cn[k]] = v
  return d

def  sen_for_doc(sentences, nlp):
  content = []
  for s in sentences:
    doc = nlp(s)
    kg = explain(doc._.kg)
    analysis = trs(doc, doc._.structure, lang)
    _data = {
      "sentence": s,
      "kg": kg,
      "analysis": analysis
    }
    content.append(_data) 
  return content


def test_save_for_doc():
  data = get_lang_sens(lang) 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["VERB"]})
  nlp.add_pipe('structure')

  for name, sentences in data.items():
    content = sen_for_doc(sentences, nlp) 
    write_to_json("tbr/doc_"+name+".json", content)


