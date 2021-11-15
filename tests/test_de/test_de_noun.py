import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

common = [
]

noun_kasus_sentences = common + [
  "In unserem Krankenhaus kann man viele Organe einschließlich des Herzens transplantieren.",
  "Gib mir bitte den Kugelschreiber.",
  "Kommst du mit der U-Bahn?",
  "Leg das Buch bitte in die Tasche.",
  "Siehst du die Maus?",
]

def test_noun_kasus():
  sentences = noun_kasus_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_kasus"]})
  display(sentences, nlp)

noun_genus_sentences = common + [
  "Gib mir bitte den Kugelschreiber.",
  "Kommst du mit der U-Bahn?",
  "Leg das Buch bitte in die Tasche.",
  "Siehst du die Maus?",
]

def test_noun_genus():
  sentences = noun_genus_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_genus"]})
  display(sentences, nlp)

noun_pluralform_sentences = common + [
  "In unserem Krankenhaus kann man viele Organe einschließlich des Herzens transplantieren.",
  "Hast du die Schlüssel?",
]

def test_noun_pluralform():
  sentences = noun_pluralform_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_pluralform"]})
  display(sentences, nlp)


_sentences = noun_kasus_sentences + noun_genus_sentences + noun_pluralform_sentences

def test_noun():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  display(sentences, nlp)


