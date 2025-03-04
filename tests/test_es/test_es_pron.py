import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

pron_ablativo_sentences = [
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
  "El ejercicio de ese derecho llevaba consigo deberes y responsabilidades especiales.",
]

def test_pron_ablativo():
  sentences = pron_ablativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_ablativo"]})
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
	"Los compré en ese supermercado.",
	"¿La has visto últimamente?",
	"Mis padres las echaron mucho de menos durante sus vacaciones.",
	"Os llamarán cuando esté todo listo.",
	"Los ordené alfabéticamente.",
	"Para el casamiento, la maquilló su hermana.",
	"Muchas gracias por el consejo, lo tendré en cuenta.",
	"Lo mandé por correo.",
	"Me lo explicó muy bien el profesor.",
	"Os tendré en cuenta para la próxima vez.",
	"Los fui a buscar en auto porque se largó a llover.",
	"Esta vez, lo voy a anotar así no me olvido de nada.",
	"Cuando sepa algo, os haré saber.",
	"Las tendré en cuenta para la próxima ocasión.",
	"Los llevé a la casa de Juanito.",
	"Nunca me lo avisaron.",
]

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
	"Nos avisaron que se había desocupado una habitación.",
	"Te llamé varias veces, pero no estabas.",
	"Me invitaron varias veces a participar, pero nunca puedo.",
	"Si no te molesta, te voy a dar un consejo.",
	"Le avisé que no podremos ir hasta mañana.",
	"En el hotel nos dieron un desayuno delicioso.",
	"Os sugiero que partan antes de que empiece a oscurecer.",
	"Les conté a mis padres que nos mudaremos el año que viene.",
	"Me han contado lo sucedido.",
	"Les regalé un chocolate.",
	"En esta ocasión, me ha tocado a mí hablar delante de todos.",
	"Quiero que te vaya bien.",
	"A los niños les encanta bailar.",
	"No os preocupes porque hay lugar para todos.",
	"Les cantaré una canción.",
	"No me interesa nada de esto.",
	"Quería que les compara un refresco.",
]

def test_pron_personales_de_objeto():
  sentences = pron_personales_de_objeto_directo_sentences 
  sentences = pron_personales_de_objeto_indirecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personales_de_objeto"]})
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
  "No, el nuestro es más grande.",
  "El suyo es azul.",
  "Las mías son más pequeñas.",
  "No, el tuyo está más atrás.",
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

_sentences = pron_ablativo_sentences + pron_personales_de_objeto_directo_sentences + pron_personales_de_objeto_indirecto_sentences 
_sentences = _sentences + pron_posesivo_sentences + pron_reflexivo_sentences


def test_pron():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PRON"]})
  display(sentences, nlp)


