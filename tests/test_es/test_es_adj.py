import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

adj_comparativo_sentences = [
  "Cristina es más simpática que Marina.",
  "Juan es más alto que Pedro.",
  "Este libro es menos interesante que aquel.",
  "Este vino es mejor que aquel.", 
  "Mi hermano es mayor que yo.",
  "Marieta es más vieja que parece.",
]

def test_adj_comparativo():
  sentences = adj_comparativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_comparativo"]})
  display(sentences, nlp)

adj_igualdad_comparativo_sentences = [
  "Ella es tan inteligente como su hermana.",
  "Ana es tan alta como su madre.",
  "Ana es igual de estudiosa que Sofía.",
  "Mis hermanas son igual de altas.",
  "Este coche es igual de viejo que ese.",
  "La producción consistente de baño de impregnación es igual de importante que el tratamiento térmico del tejido.",
  "La familia de la niña es igual de pobre que ellos.",
  "Los demás vehículos son iguales de lujosos.",
  "Todos los políticos son iguales de corruptos.",
]

def test_adj_igualdad_comparativo():
  sentences = adj_igualdad_comparativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_igualdad_comparativo"]})
  display(sentences, nlp)


adj_superlativo_sentences = [
  "Ella es la más inteligente de la clase.",
  "Este es el menos caro de todos.",
  "Lucas es el más simpático de sus amigos.",
  "Julia es la chica más alegre que conozco.",
  "Santiago y Pedro son los peores estudiantes de la clase.",
  "Rosa es la mejor jugadora de su equipo.",
  "Este es el cuadro más perfecto que alguien haya hecho.",
  "Esta es la carretera más lenta de todo el estado.",
  "Él es el mejor director de cine de todos los tiempos.",
  "La escalada es uno de los deportes más peligrosos.",
  "Las ruinas de Machu Picchu son las más impresionantes que he visto.",
  "Para mí, el café de Colombia es el mejor del mundo.",
]

def test_adj_superlativo():
  sentences = adj_superlativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_superlativo"]})
  display(sentences, nlp)


adj_absoluto_superlativo_sentences =[
  "Este pastel es riquísimo.",
  "La película fue interesantísima.",
]

def test_adj_absoluto_superlativo():
  sentences = adj_absoluto_superlativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_absoluto_superlativo"]})
  display(sentences, nlp)

adj_demostrativo_sentences = [
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

def test_adj_demostrativo():
  sentences = adj_demostrativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_demostrativo"]})
  display(sentences, nlp)

adj_posesivo_sentences = [
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


def test_adj_posesivo():
  sentences = adj_posesivo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_posesivo"]})
  display(sentences, nlp)

_sentences = adj_comparativo_sentences + adj_igualdad_comparativo_sentences + adj_superlativo_sentences + adj_absoluto_superlativo_sentences
_sentences = _sentences + adj_demostrativo_sentences + adj_posesivo_sentences


def test_adj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  display(sentences, nlp)

