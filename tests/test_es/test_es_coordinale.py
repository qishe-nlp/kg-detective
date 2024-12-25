import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

coordinales_sentences = [
  "Es el cumpleaños de su novia, pero no tiene dinero para celebrarlo.",
  "Ni me llama ni me escribe.",
  "No me lo pidas a mí, sino a él.",
  "Tiene mucho sueño, pero tiene un examen mañana.",
  "Podemos ir ver la nueva peli mañana u otro día.",
  "Yo me vestiré e iré con ustedes.",
  "¿Pagas la cuenta o te pongo una demanda?",
  "No lloverá y hará un buen día.",
  "Tiene muchos libros en su casa, pero nunca lee.",
  "Llegaron los obreros e hicieron el trabajo.",
]

def test_coordinales():
  sentences = coordinales_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["coordinale"]})
  display(sentences, nlp)

_sentences = coordinales_sentences


def test_():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["COORDINALE"]})
  display(sentences, nlp)


