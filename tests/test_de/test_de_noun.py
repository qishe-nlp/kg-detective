import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

common = [
  "Was passt nicht ? Die Katze spielt mit die Maus.",
  "Was passt nicht ? Hast duder Schlüssel?",
  "Was passt nicht ? Hier ist den Bäcker.",
  "Was passt nicht ? Bist du fertig mit der Brief?",
  "In unserem Krankenhaus kann man viele Organe einschließlich des Herzens transplantieren. ",
  "Hast du die Schlüssel?",
  "Gib mir bitte den Kugelschreiber.",
  "Kommst du mit der U-Bahn?",
  "Leg das Buch bitte in die Tasche.",
  "Siehst du die Maus?",
]

noun_kasus_sentences = common + [
]

def test_noun_kasus():
  sentences = noun_kasus_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_kasus"]})
  display(sentences, nlp)

noun_genus_sentences = common + [
]

def test_noun_genus():
  sentences = noun_genus_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_genus"]})
  display(sentences, nlp)

noun_pluralform_sentences = common + [
]

def test_noun_pluralform():
  sentences = noun_pluralform_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_pluralform"]})
  display(sentences, nlp)

def test_noun():
  sentences = noun_kasus_sentences + noun_genus_sentences + noun_pluralform_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  display(sentences, nlp)


