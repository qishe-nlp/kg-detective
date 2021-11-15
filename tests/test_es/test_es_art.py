import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

art_determinado_sentences = [
  "Las águilas son aves.",
  "Montevideo es la capital de Uruguay.",
  "Queremos ver al jefe de estudios.",
  "El agua es mi bebida preferida.",
  "Los padres de Sofía viven en Lima.",
  "Los norteamericanos hablan inglés.",
  "Me gustan las naranjas.",
  "Escribe en la pizarra, por favor.",
  "Ese coche es del padre de Mónica.",
  "Vivimos cerca del centro.",
]

def test_art_determinado():
  sentences = art_determinado_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_determinado"]})
  display(sentences, nlp)

art_indeterminado_sentences = [
  "Un melón, por favor.",
  "¡Cuidado, una serpiente!",
  "¡Mira, un águila!",
  "Es una radio.",
  "¿Tienes un mapa de Ecuador?",
  "Rosa tiene una hija.",
  "Tenemos unos cincuenta euros.",
  "Susana tiene unos treinta años.",
  "Necesito que me eches una mano.",
  "El tulipán es una flor.",
]


def test_art_indeterminado():
  sentences = art_indeterminado_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_indeterminado"]})
  display(sentences, nlp)

art_omisión_sentences = [
  "Prefiero las de algodón.",
  "Prefiero la de verduras.",
  "Yo quiero uno nuevo.",
  "Necesito unas más grandes.",
  "¿Prefieres los guantes de lana o los de cuero?",
  "Prefiero el vino de Valdepeñas o el de Rioja.",
  "Los de plata.",
  "Trae unos limpios.",
  "Es mejor el de mi padre.",
  "Prefiero la de chocolate.",
]

def test_art_omisión():
  sentences = art_omisión_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_omisión"]})
  display(sentences, nlp)


_sentences = art_determinado_sentences + art_indeterminado_sentences + art_omisión_sentences


def test_art():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ART"]})
  display(sentences, nlp)


