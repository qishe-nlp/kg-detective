import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

num_cardinales_sentences = [
  "Las entradas cuestan veintiún euros.",
  "Uno de mayo.",
  "En esta clase hay veintiuna alumnas.",
  "Una.",
  "El periódico cuesta un euro.",
  "La Habana tiene dos millones de habitantes.",
  "María gana dos mil ochenta y cinco euros al mes.",
  "Más de trescientas.",
  "La mujer más vieja del mundo tiene ciento veintiún años.",
  "Mil doscientos setenta y cuatro kilómetros.",
]

def test_num_cardinales():
  sentences = num_cardinales_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["num_cardinales"]})
  display(sentences, nlp)

num_división_y_fracciones_sentences = [
  "Dos más dos son cuatro.",
  "Siete menos cuatro son tres.",
  "Tres por seis son dieciocho.",
  "Treinta entre cinco son seis.",
]

def test_num_división_y_fracciones():
  sentences = num_división_y_fracciones_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["num_división_y_fracciones"]})
  display(sentences, nlp)

num_horas_y_fechas_sentences = [
  "Ahora son las once y cinco.",
  "Quedamos a las cuatro menos veinticinco.",
  "Es la una y diez.",
  "Estamos a veinte de abril.",
  "Hoy es jueves 25 de abril de 2002.",
  "Se casó el 9 de abril de 1954.",
]

def test_num_horas_y_fechas():
  sentences = num_horas_y_fechas_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["num_horas_y_fechas"]})
  display(sentences, nlp)


num_múltiplos_sentences = [
  "Esto es solo una décima parte de lo que tienes que hacer.",
  "Compra medio kilo de manzanas.",
  "Juan está el doble de gordo que hace un año.",
  "A Antonio le corresponde un quinto de la herencia.",
  "Teresa gana el triple que yo.",
  "Dame la mitad de ese bocadillo.",
  "Esto es el doble de lo que yo esperaba.",
  "Ana gana la mitad que yo.",
  "Eso es dos veces menos de lo que me dijiste.",
  "La mitad de nosotros trabajamos en una empresa.",
]

def test_num_múltiplos():
  sentences = num_múltiplos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["num_múltiplos"]})
  display(sentences, nlp)

num_ordinales_sentences = [
  "Enero es el primer mes del año.",
  "El Valencia es el primero en la Liga de fútbol.",
  "Javi es el tercero de sus hermanos.",
  "Yo soy la quinta de mis seis hermanas.",
  "Las hijas de Carlos son las primeras de la clase.",
  "Tina y Carla acabaron cuartas en el campeonato de tenis.",
  "Fuimos los primeros en llegar a la fiesta.",
  "Es la segunda vez que salgo con Marta.",
  "Ana y Rosa fueron las segundas clasificadas por equipos.",
  "Es la cuarta película que vemos esta semana.",
  "Teresa y su hermana quedaron décimas en el concurso del colegio.",
]


def test_num_ordinales():
  sentences = num_ordinales_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["num_ordinales"]})
  display(sentences, nlp)

_sentences = num_cardinales_sentences + num_división_y_fracciones_sentences + num_horas_y_fechas_sentences
_sentences = _sentences + num_múltiplos_sentences + num_ordinales_sentences


def test_num():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NUM"]})
  display(sentences, nlp)


