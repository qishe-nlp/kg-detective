import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

adv_afirmación_y_negación_sentences = [
  "Qué va, nunca bebo.",
  "Elena nunca sale de noche.",
  "Su hermano tampoco.",
  "A mí no, es demasiado picante.",
  "Este año no tengo vacaciones.",
  "Yo sí, pero en septiembre.",
  "Mañana no trabajo.",
  "Yo sí, trabajo todos los días.",
  "No sé conducir.",
  "Yo tampoco.",
  "Tú también, Marisa.",
  "Nosotras también.",
  "Yo no.",
  "Luis no sabe jugar al tenis.",
  "Pues Ramón sí.",
]

def test_adv_afirmación_y_negación():
  sentences = adv_afirmación_y_negación_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_afirmación_y_negación"]})
  display(sentences, nlp)

adv_cantidad_sentences = [
  "Es muy buena.",
  "No se puede oír nada. La música está demasiado alta.",
  "Este libro no es nada caro.",
  "Rubén es demasiado sincero.",
  "Silvia se lleva muy bien con su hermana.",
  "Suelo desayunar muy poco: un café con leche nada más.",
  "Rosa y yo nos vemos mucho, casi todas las semanas.",
  "Me duele mucho la cabeza.",
  "Nacho no ayuda mucho a sus padres.",
  "María no estudia mucho.",
]

def test_adv_cantidad():
  sentences = adv_cantidad_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_cantidad"]})
  display(sentences, nlp)

adv_comparativa_sentences = [
  "No hables tan alto, por favor.",
  "Habla más bajo.",
  "Vas muy rápido.",
  "No vayas tan rápido.",
  "Ve más lento.",
  "No trabajen tanto.",
  "Trabajen menos.",
  "No gritéis tanto.",
  "Hablo español bien, pero Li habla mejor que yo.",
  "Jorge estudiaba mucho y ahora estudia tanto como antes.",
  "Duermo mucho, pero María duerme más que yo.",
  "Alberto habla mucho y su mujer habla tanto como él.",
  "Enrique bebe poco, pero Manuel bebe aún menos que él.",
]

def test_adv_comparativa():
  sentences = adv_comparativa_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_comparativa"]})
  display(sentences, nlp)


adv_frecuencia_sentences = [
  "Casi nunca salgo con Teresa.",
  "Normalmente, suelo cenar en casa.",
  "Me levanto siempre a las siete.",
  "Vamos mucho al cine, tres o cuatro veces al mes.",
  "Nunca me acuesto antes de las doce.",
  "Mis padres hacen un viaje de vez en cuando, dos o tres veces al año.",
  "¿Ves mucho a Lola?",
  "De vez en cuando.",
  "Ernesto come siempre en casa.",
  "Viajo frecuentemente a Argentina.",
  "¿Van mucho a la disco?",
  "Una vez al mes o algo así.",
]

def test_adv_frecuencia():
  sentences = adv_frecuencia_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_frecuencia"]})
  display(sentences, nlp)

adv_lugar_sentences = [
  "El perro está fuera de la casa.",
  "Cerca de tu casa hay un centro comercial.",
  "Tus zapatos están debajo de ese mueble.",
  "Enfrente del colegio hay un edificio enorme.",
  "Hay una sorpresa dentro de la caja.",
  "Cristina está sentada frente a Paula.",
  "El chico que está detrás de ti, es mi hermano.",
  "Ya empieza la película, vamos adentro.",
  "Nicolás está durminedo encima de la alfombra.",
  "Una mariposa vuela alrededor de las flores.",
]


def test_adv_lugar():
  sentences = adv_lugar_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_lugar"]})
  display(sentences, nlp)

adv_modo_sentences = [
  "Lorena no conduce bien.",
  "A Rubén le gusta cantar aunque canta muy mal.",
  "Elisa habla muy rápido, casi no le entienden nada.",
  "Manuel resultó herido gravemente en el accidente.",
  "Juan siempre hace su trabajo rápida y eficazmente.",
  "No hables tan alto por favor.",
  "Alex es un chico majo pero a veces se porta mal con sus amigos.",
  "Mario canta muy bien.",
  "Noelia conoce Cuba perfectamente.",
  "Conduce muy mal.",
]

def test_adv_modo():
  sentences = adv_modo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_modo"]})
  display(sentences, nlp)

adv_tiempo_sentences = [
  "Estoy segura de que nos veremos pronto.",
  "Mañana nos tenemos que levantar temprano.",
  "Llamamos al timbre y después salió el marido de Tere.",
  "Habéis llegado tarde.",
  "La película ya ha empezado.",
  "Daos prisa. Los invitados van a llegar pronto.",
  "Pablo y yo ya no salimos juntos.",
  "Cuidado. La sopa todavía está caliente.",
  "Estoy esperando a Lidia desde las seis, pero todavía no ha llegado.",
  "Todavía no lo sé.",
  "Sí, ya lo sé.",
]


def test_adv_tiempo():
  sentences = adv_tiempo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_tiempo"]})
  display(sentences, nlp)


_sentences = adv_afirmación_y_negación_sentences + adv_cantidad_sentences + adv_comparativa_sentences + adv_frecuencia_sentences
_sentences = _sentences + adv_lugar_sentences + adv_modo_sentences + adv_tiempo_sentences


def test_adv():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADV"]})
  display(sentences, nlp)


