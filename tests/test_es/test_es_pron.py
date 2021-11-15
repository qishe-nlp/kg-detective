import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

pron_ablativos_sentences = [
  "Nuestros hijos vienen con nosotros a todas partes.",
  "Tengo algo para ellas.",
  "Según tú y tus amigos, yo tengo la culpa.",
  "¿Vienes conmigo?",
  "Un chico pregunta por ella.",
  "Entre tú y yo: aquí todos están locos.",
  "Tengo algo para ti.",
  "Todos quieren que me vaya, hasta tú, Pedro.",
  "¿Un paquete para mí?",
  "Quiero bailar contigo.",
]

def test_pron_ablativos():
  sentences = pron_ablativos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_ablativos"]})
  display(sentences, nlp)

pron_demostrativo_sentences = [
  "¿Es esto suyo? Estaba en el suelo.",
  "¡Eso no es verdad!",
  "Léeme esto, por favor.",
  "No sé por qué dices eso.",
  "Lleva esto a tu madre.",
  "En esta habitación hay dos camas.",
  "Mira, te presento, esta es mi hermana.",
  "¿Cómo son aquellas negras?",
  "Sí, este rubio y aquel alto, al lado del árbol.",
  "Escucha esto: 'Han detenido a dos personas de una tienda...'",
]


def test_pron_demostrativo():
  sentences = pron_demostrativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_demostrativo"]})
  display(sentences, nlp)

pron_indefinido_sentences = [
  "Todas tienen alas muy bonitas.",
  "Están todos en el jardín.",
  "Se la han comido toda.",
  "Es igual. Me gustan todos.",
  "Se la han bebido toda.",
  "No, enséñeme otros, por favor.",
  "No he encontrado mis llaves, pero Juan tiene otras.",
  "¿Cuándo hay otro?",
  "Coge uno si quieres.",
  "Préstame una.",
]

def test_pron_indefinido():
  sentences = pron_indefinido_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_indefinido"]})
  display(sentences, nlp)


pron_interrogativo_sentences = [
  "¿Quién es tu profesor?",
  "¿Quiénes son las amigas de Ana?",
  "¿Qué llevas en la bolsa?",
  "¿Quién tiene mi diccionario?",
  "¿Qué te dijo Sofía?",
  "¿Cuál de tus hermanos trabaja en Aerolíneas?",
  "¿Cuál es tu comida preferida?",
  "¿Qué deportes practicas?",
  "¿En qué ciudad de México vive María?",
  "¿Con qué líneas aéreas va a viajar Sol?",
]

def test_pron_interrogativo():
  sentences = pron_interrogativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_interrogativo"]})
  display(sentences, nlp)

pron_personales_de_objeto_directo_sentences = [
  "Sí, lo amo.",
  "No, no la quiero.",
  "No, no las he visto.",
  "¿Me recuerdas?",
  "Sí, te recuerdo.",
  "Sí, los veo mucho.",
  "¿Te quiere Elena?",
  "No, no me quiere.",
  "No, no los conozco.",
  "¿Te conocen en esta tienda?",
  "Sí, me conocen mucho.",
  "Sí, los quiero.",
  "No, no la quiero.",
]


def test_pron_personales_de_objeto_directo():
  sentences = pron_personales_de_objeto_directo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personales_de_objeto_directo"]})
  display(sentences, nlp)

pron_personales_de_objeto_indirecto_sentences = [
  "¿Qué te han dicho?",
  "No me ha dicho nada.",
  "¿Qué le ha dicho a usted?",
  "No me ha dicho nada.",
  "¿Qué os ha dado?",
  "No nos ha dicho nada.",
  "¿Qué le han preguntado a Susana?",
  "No le ha preguntado nada.",
  "¿Qué me ha dicho?",
  "No te ha dicho nada.",
  "¿Qué nos han preguntado?",
  "No os ha preguntado nada.",
  "¿Qué te ha vendido?",
  "Me ha vendido unas flores.",
  "¿Qué les han dado a ustedes?",
  "Nos han dado un sobre con llaves.",
  "¿Qué le han preguntado a Alberto?",
  "Le han preguntado por su madre.",
  "¿Qué les han regalado a tus hijas?",
  "Les han regalado dos muñecas.",
]

def test_pron_personales_de_objeto_indirecto():
  sentences = pron_personales_de_objeto_indirecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personales_de_objeto_indirecto"]})
  display(sentences, nlp)

pron_personales_de_sujeto_sentences = [
  "¿De dónde sois Adolfo y tú ?",
  "Nosotros somos de Uruguay.",
  "Perdone, ¿de dónde son ustedes?",
  "Nosotros somos de Arequipa.",
  "Nosotros estudiamos Medicina.",
  "Yo quiero un café, y vosotros ¿qué queréis?",
  "Ellas son amigas de Blanca.",
  "Yo trabajo todo el día y vosotras no hacéis nada.",
  "¿Quiere usted algo, Sr. Hernández?",
  "Él está en su habitación.",
  "Yo. Lo necesito unos minutos.",
  "Tú eres la ganadora.",
]

def test_pron_personales_de_sujeto():
  sentences = pron_personales_de_sujeto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personales_de_sujeto"]})
  display(sentences, nlp)

pron_posesivo_sentences = [
  "No, el mío es gris.",
  "No, las suyas son en color.",
  "El nuestro está averiado.",
  "Está bien, pero el mío es mejor.",
  "¿Y la tuya?",
  "La mía es de Ávila.",
  "¿Dónde está la tuya?",
  "El suyo es negro.",
  "No, el suyo es más grande.",
  "No, la nuestra es rubia.",
  "No, las nuestras las tiene Ángel.",
]

def test_pron_posesivo():
  sentences = pron_posesivo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_posesivo"]})
  display(sentences, nlp)

pron_reflexivo_sentences = [
  "Me ducho todos los días.",
  "Mi profesora se pone una bata en clase.",
  "Roberto y Pablo se acuestan siempre tarde.",
  "No nos levantamos nunca temprano.",
  "Los domingos lavo el pelo a Ana.",
  "¿Dónde os bañasteis ayer?",
  "María se mira mucho al espejo.",
  "¿Cuándo te afeitas?",
]

def test_pron_reflexivo():
  sentences = pron_reflexivo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_reflexivo"]})
  display(sentences, nlp)

pron_relativo_sentences = [
  "Rocío es la dueña de la casa donde vive Matías.",
  "Son los domingos cuando más gente viene.",
  "Esta es la dirección adonde tienes que mandar el paquete.",
  "Haz el ejercicio como lo hace la profesora.",
  "Normalmente es a las dos cuando comemos.",
  "Fue en Colombia donde conocí a mi marido.",
  "¿Cuál es el pueblo adonde vais en verano?",
  "La película acabó como yo pensaba. Se casan.",
  "Este es el hotel donde nos alojamos el año pasado.",
  "Recuerdo una época cuando no había muchos coches en Madrid.",
]

def test_pron_relativo():
  sentences = pron_relativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_relativo"]})
  display(sentences, nlp)


_sentences = pron_ablativos_sentences + pron_demostrativo_sentences + pron_indefinido_sentences + pron_interrogativo_sentences
_sentences = _sentences + pron_personales_de_objeto_directo_sentences + pron_personales_de_objeto_indirecto_sentences + pron_personales_de_sujeto_sentences
_sentences = _sentences + pron_posesivo_sentences + pron_reflexivo_sentences + pron_relativo_sentences


def test_pron():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PRON"]})
  display(sentences, nlp)


