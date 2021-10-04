import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

zahl_grund_sentences = [
  "Neun plus sieben ist sechzehn.",
  "Es kostet zehn Euro fünfzehn.",
  "Es ist acht Uhr zwanzig.",
]

def test_zahl_grund():
  sentences = zahl_grund_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_grund"]})
  display(sentences, nlp)


zahl_ordnung_sentences = [
  "Der erste Weltkrieg begann im Jahr 1914.",
  "Heute ist der 16. Mai.",
  "Ich habe am 7. Juli Geburtstag.",
]

def test_zahl_ordnung():
  sentences = zahl_ordnung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_ordnung"]})
  display(sentences, nlp)

zahl_verteilung_sentences = [
  "Ich komme nicht mit. Erstens habe ich keine Zeit und zweitens habe ich Keine Lust.",
]

def test_zahl_verteilung():
  sentences = zahl_verteilung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_verteilung"]})
  display(sentences, nlp)

zahl_wiederholung_sentences = [
  "Waren Sie schon einmal in Deutschland?",
  "Das ist doch eine einmalige Chance.",
]


def test_zahl_wiederholung():
  sentences = zahl_wiederholung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_wiederholung"]})
  display(sentences, nlp)

zahl_vervielfältigung_sentences = [
  "Er hat sich bei mir dafür mehrfach.",
]

def test_zahl_vervielfältigung():
  sentences = zahl_vervielfältigung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_vervielfältigung"]})
  display(sentences, nlp)

zahl_bruch_sentences = [
  "Es ist Viertel nach sechs.",
  "Ich möchte ein halbes Pfund Butter.",
  "Es dauert anderthalb Stunden.",
]

def test_zahl_bruch():
  sentences = zahl_bruch_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["zahl_bruch"]})
  display(sentences, nlp)


def test_zahl():
  sentences = zahl_grund_sentences + zahl_ordnung_sentences + zahl_verteilung_sentences + zahl_wiederholung_sentences
  sentences = sentences + zahl_vervielfältigung_sentences + zahl_bruch_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ZAHL"]})
  display(sentences, nlp)


