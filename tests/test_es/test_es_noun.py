import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

noun_comparativa_sentences = [
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

def test_noun_comparativa():
  sentences = noun_comparativa_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_comparativa"]})
  display(sentences, nlp)

noun_géneros_sentences = [
  "El bebé es una niña.",
  "Juan es una buena persona.",
  "Rodolfo Valentino fue una estrella del cine.",
  "¿Cómo se llama la víctima?",
  "El personaje principal de la novela es una mujer.",
  "¿Es un gorila macho o hembra?",
  "Hay una serpiente en aquel árbol.",
  "Una jirafa macho es más alta que una jirafa hembra.",
  "Un caracol.",
  "La mariposa es un insecto.",
]


def test_noun_géneros():
  sentences = noun_géneros_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_géneros"]})
  display(sentences, nlp)

noun_números_sentences = [
  "Este río está lleno de peces.",
  "Me han regalado dos pares de medias.",
  "El lunes es fiesta.",
  "Las tijeras no cortan.",
  "Necesito unos pantalones.",
  "No trabajo nunca los lunes.",
  "Me he comprado un par de pantalones.",
  "El virus de la gripe es muy potente.",
  "Se me ha roto el paraguas.",
  "Se me han roto los vaqueros.",
]

def test_noun_números():
  sentences = noun_números_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_números"]})
  display(sentences, nlp)


noun_propios_sentences = [
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

def test_noun_propios():
  sentences = noun_propios_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_propios"]})
  display(sentences, nlp)

_sentences = noun_comparativa_sentences + noun_géneros_sentences + noun_números_sentences + noun_propios_sentences

def test_noun():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  display(sentences, nlp)


