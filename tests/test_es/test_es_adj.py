import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

adj_comparativa_sentences = [
  "Cristina es más simpática que Marina.",
  "Lucas es el más simpático de sus amigos.",
  "Julia es la chica más alegre que conozco.",
  "Marieta es más vieja que parece.",
  "Para mí, el café de Colombia es el mejor del mundo.",
  "Santiago y Pedro son los peores estudiantes de la clase.",
  "Las ruinas de Machu Picchu son las más impresionantes que he visto.",
  "Mis hermanas son igual de altas.",
  "Ana es tan alta como su madre.",
  "Ana es igual de estudiosa que Sofía.",
]

def test_adj_comparativa():
  sentences = adj_comparativa_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_comparativa"]})
  display(sentences, nlp)

adj_demostrativos_sentences = [
  "Este verano vamos a ir a Ibiza.",
  "Son muy caros estos zapatos. Vamos a ver otros.",
  "¿Qué vais a hacer este domingo?",
  "Ese verano conocí a Lu.",
  "Aquellos años fueron los mejores años de su vida.",
  "Perdone, ¿está libre esta silla?",
  "En aquella época no trabajaba.",
  "Esta semana ha sido agotadora.",
  "Ese día regresan mis padres.",
  "Fíjate en aquel chico que está al lado de la puerta, es muy guapo.",
]


def test_adj_demostrativos():
  sentences = adj_demostrativos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_demostrativos"]})
  display(sentences, nlp)

adj_género_y_número_sentences = [
  "Alberto tiene la nariz grande.",
  "Me gustan los coches veloces.",
  "Luisa es una persona encantadora.",
  "Luisa y su hermano son rubios.",
  "Estoy cansada.",
  "Ha sido un día agotador.",
  "Rosa y Luis están divorciados.",
  "Me he comprado una falda marrón.",
  "Necesito una talla mayor.",
  "¿Dónde está mi camisa gris?",
  "Compra esa otra cámara.",
  "Es mejor.",
]

def test_adj_género_y_número():
  sentences = adj_género_y_número_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_género_y_número"]})
  display(sentences, nlp)


adj_indefinidos_sentences = [
  "Conozco a toda tu familia, Pedro.",
  "Todas sus maletas están ya en el coche, Don Manuel.",
  "Lucas gasta todo el dinero en novelas.",
  "¿Dónde están todos los alumnos, Srta.",
  "Todos nuestros amigos nos quieren mucho.",
  "Con todas mis amigas.",
  "Hoy no puedo, pero podemos ir otro día.",
  "Ponte otros zapatos.",
  "Son demasiadas.",
  "Tenemos muy poco tiempo.",
]

def test_adj_indefinidos():
  sentences = adj_indefinidos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_indefinidos"]})
  display(sentences, nlp)

adj_posesivos_sentences = [
  "¿Cuál es tu color preferido, Berta?",
  "Mi hermano y yo jugamos mucho al tenis.",
  "Es nuestro deporte preferido.",
  "La señora Valverde y sus hijas son muy simpáticas.",
  "Tenéis los ojos rojos.",
  "Estas llaves no son mías.",
  "Las mías son más pequeñas.",
  "¿Es ese vuestro coche?",
  "No, el nuestro es más grande.",
  "El suyo es azul.",
  "Perdona, ¿es este mi asiento?",
  "No, el tuyo está más atrás.",
  "Son nuestros.",
]


def test_adj_posesivos():
  sentences = adj_posesivos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_posesivos"]})
  display(sentences, nlp)

_sentences = adj_comparativa_sentences + adj_demostrativos_sentences + adj_género_y_número_sentences + adj_indefinidos_sentences
_sentences = _sentences + adj_posesivos_sentences
# + xxxx_sentences


def test_adj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  display(sentences, nlp)


