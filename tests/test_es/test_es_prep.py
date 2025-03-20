import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

prep_con_adjetivo_sentences = [
  "Alberto es muy generoso con sus amigos.",
  "¿Tú crees que Daniel es incapaz de hacerte esa faena?",
  "Es muy orgulloso por sus hijos.",
  "La ciudad está rodeada de montañas y bosques.",
  "Estoy conforme con mi suerte.",
  "La historia es demasiado larga para contar.",
  "El agua es algo esencial para la vida.",
  "Juana no está satisfecha con el resultado del examen.",
  "Iré acompañado de unos amigos.",
  "La vuelta a la calma ha ido acompañada de un refuerzo de la censura.",
  "Llegué exhausta pero contenta a Ciudad Guatemala.",
  "Mi hija va loca por Halloween Juegos.",
  "Que en Madrid ha peinado a lo mejor de cada casa.",
  "Eso o empiezo a cobrar el doble por habitación.",
  "¿Pero la tercera desde dónde?",
  "Entra, entra, chiquilla, y cuéntamelo todo, que estoy mala sin saber qué ha pasado.",
]


def test_prep_con_adjetivo():
  sentences = prep_con_adjetivo_sentences 
  #sentences = more
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_con_adjetivo"]})
  display(sentences, nlp)

prep_con_verbo_sentences = [
  "¿Confías en nosotros?",
  "Lina se ha divorciado de su marido.",
  "¿Te atreves a tirarte desde aquí?",
  "Esther se ha enfadado con Amelia.",
  "¿Cuándo van a comenzar a pintar la casa?",
  "Me alegro mucho de verte.",
  "Tengo que aprender a conducir.",
  "¿Crees en las supersticiones?",
  "La policía sospecha de la enfermera.",
  "Bruno y Adela no se deciden a casarse.",
]

ai_created = [
  "Tienes que enfrentarte a tu destino.",
  "Miro a la pantalla.",
  "Llegamos a la estación.",
  "Ellos suben a la montaña.",
  "Me acerco a la puerta.",
  "Debemos atacar al problema.",
  "Ella responde a la pregunta.",
  "Amamos a la naturaleza.",
  "Escucho a la música.",
  "Vuelvo a la casa.",
  "Entramos a la habitación.",
 ]

def test_prep_con_verbo():
  sentences = prep_con_verbo_sentences 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_con_verbo"]})
  display(sentences, nlp)

_sentences = prep_con_adjetivo_sentences + prep_con_verbo_sentences

def test_prep():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PREP"]})
  display(sentences, nlp)


