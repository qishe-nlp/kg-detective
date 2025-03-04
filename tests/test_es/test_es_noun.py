import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

noun_comparativo_sentences = [
  "Hay menos de veinticinco personas.",
  "Necesitamos más comida.",
  "Compra menos naranjas.",
  "Había más de mil personas.",
  "No pagues más de cincuenta euros.",
  "Tiene más de quinientas.",
  "Necesitamos más sillas.",
  "Si cuesta menos de diez euros, es barato.",
  "Tiene menos de dieciocho años.",
  "Tienes que trabajar menos horas.",
]

def test_noun_comparativo():
  sentences = noun_comparativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_comparativo"]})
  display(sentences, nlp)

noun_propio_sentences = [
  "La capital de la provincia de Buenos Aires es La Plata.",
  "Martín llevó a su perro Toby al veterinario.",
  "La próxima reunión de la Organización de las Naciones Unidas tendrá ese tema como eje central.",
  "Antes de morir, debes conocer las ruinas de Machu Pichu.",
  "La Torre Eiffel fue lo más llamativo de nuestro viaje.",
  "Este año no me voy a perder el concierto de Ed Sheeran en el Teatro Gran Rex.",
  "Si vienes, podremos hacer un viaje a la Patagonia.",
  "El verano pasado recorrimos Europa.",
  "Tienes que ver lo bonito que es el nieto de María del Carmen.",
]

def test_noun_propio():
  sentences = noun_propio_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_propio"]})
  display(sentences, nlp)

_sentences = noun_comparativo_sentences + noun_propio_sentences

def test_noun():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  display(sentences, nlp)


