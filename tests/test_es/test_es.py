import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
#from tests.constants import tbr_en_sentences as _sentences
from importlib import import_module
import os.path, pkgutil

lang = "es"
pkg = PKG_INDICES[lang]

_sentences = get_lang_sens(lang)["test_es_adv"] 

def test_es_kg():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg')
  display(sentences, nlp)


