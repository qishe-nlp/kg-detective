import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

conj_einfache_sentences = [
  "Ich heiße Thomas Bahr und ich bin der Vater von Lisa und Felix.",
  "Früher habe ich in Bonn gelebt, aber jetzt lebe ich in Berlin.",
  "Ich habe eine Tochter und einen Sohn.",
  "Meine Tochter heißt Lisa. Sie will in London studieren oder in Dublin.",
  "In seiner Freizeit trifft er sich lieber mit Freunden oder er geht schwimmen.",
  "Er geht gern schwimmen, denn er mag Wasser.",
]

def test_conj_einfache():
  sentences = conj_einfache_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["conj_einfache"]})
  display(sentences, nlp)


conj_zweiteilige_sentences = [
  "Er ist nicht nur Lehrer, sondern auch Dichter.",
  "Entweder ist er verreist, oder er ist krank.",
  "Er ist zwar klein, aber kräftig.",
  "Ich habe dafür weder Zeit noch Geld."
]

def test_conj_zweiteilige():
  sentences = conj_zweiteilige_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["conj_zweiteilige"]})
  display(sentences, nlp)


_sentences = conj_einfache_sentences + conj_zweiteilige_sentences

def test_conj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["CONJ"]})
  display(sentences, nlp)


