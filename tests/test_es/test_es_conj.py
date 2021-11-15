import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

conj_conj_sentences = [
  "¿Es usted peruano o boliviano?",
  "¿Tienes lápiz y papel?",
  "No recuerdo si dijo septiembre u octubre.",
  "Mis meses preferidos son julio y agosto.",
  "No recuerdo si me dieron diez u once.",
  "Solo conozco dos países europeos, Francia e Italia.",
  "¿Estudias y trabajas?",
  "Gabriel e Ignacio trabajan en la misma empresa.",
  "Había veinte o veinticinco personas en la sala.",
  "Ven mañana u otro día.",
]

def test_conj_conj():
  sentences = conj_conj_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["conj_conj"]})
  display(sentences, nlp)


_sentences = conj_conj_sentences

def test_conj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["CONJ"]})
  display(sentences, nlp)


