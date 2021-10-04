import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

interj_interj_sentences = [
]

def test_interj_interj():
  sentences = interj_interj_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["interj_interj"]})
  display(sentences, nlp)

def test_interj():
  sentences = interj_interj_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["INTERJ"]})
  display(sentences, nlp)


