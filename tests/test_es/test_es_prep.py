import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]

def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)

_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]


def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)

_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]

def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)


_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]

def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)

_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]


def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)

_sentences = [
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
]

def test_():
  sentences = _sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": [""]})
  display(sentences, nlp)


def test_():
  sentences = _sentences + _sentences + _sentences + _sentences
  sentences = sentences + _sentences + _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": [""]})
  display(sentences, nlp)


