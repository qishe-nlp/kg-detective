import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

interj_interj_sentences = [
  "¡Quién podía pensar en esa boda!",
  "¡Qué noche tan fría!",
  "¡Qué vago es Darío! No le gusta nada trabajar.",
  "¡Qué tarde es! Tengo que irme.",
  "¡Cómo come Isma! Se ha terminado la hamburguesa en un minuto!",
  "¡Cómo me gusta que me inviten a cenar!",
  "¡Quién iba a pensar que Blanca y José se casarían!",
  "¡Quién podía saber la verdad!",
  "¡Quién podría imaginar que nos veríamos en Cuzco!",
  "¡Qué niebla! Hoy no vamos a poder salir de viaje.",
]

def test_interj_interj():
  sentences = interj_interj_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["interj_interj"]})
  display(sentences, nlp)

_sentences = interj_interj_sentences

def test_interj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["INTERJ"]})
  display(sentences, nlp)


