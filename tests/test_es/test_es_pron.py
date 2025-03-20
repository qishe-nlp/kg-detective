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

more_1 = [
  "Lo siento, solo pudimos salvarla a usted.",
  "Yo no he estafado a nadie.",
  "No podemos localizar a nadie ahora mismo.",
  "Pero aquí no conozco a nadie.",
  "Tú a nadie, que es mucho pollo para tan poco arroz.",
]

more_2 = [
  "No, de eso olvídese.",
  "Y por eso le retengo el pasaporte.",
  "Además, tendrá que ayudarla, aquí en Tetuán no conoce a nadie y arrastra una historia bastante fea.",
  "Por eso se ha tenido que levantar el Ejército, para acabar con tanta risa, con tanta alegría y con tanto libertinaje, que estaban llevando a España a la ruina.",
  "Tú no sufras, mi alma, de eso me encargo yo.",
]

more_3 = [
  "¿ En qué voy a trabajar?",
  "¿ A quién queremos conocer?",
  "¿ De dónde sale esta chiquilla?",
  "¿ A quién llamas viejas meapilas?",
  "Pero si no hay con quién.",
  "Jamila, ¿ de quién es esta habitación?",
  "¿Andrés exactamente a qué se dedica?",
  "¿ A qué se dedica?",
  "¿ A quién no habrá peinado esta muchacha?",
  "¿ De dónde has sacado la tela?",
  "¿ A quién apunto primero?",
  "¿Y por qué iba a quitarme el vestido para alguien que no quiere ayudarme a volver a mi casa?",
  "Y no me pregunte de dónde los he sacado porque los dos sabemos que son falsos.",
  "¿ A qué se debe su visita?",
  "Palomares, yo le juro por lo más sagrado que ninguno sabía a qué se dedicaba este señor.",
  "¿Pero la tercera desde dónde?",
  "A ver por dónde nos sale el payo.",
  "¿Y a quién se las vendemos?",
  "Candelaria, ¿y usted a la guerra con quién va?",
  "Lo que todavía no entiendo es por qué me necesita a mí.",
  "¿ A qué viene esa cara?",
  "¿Pero por qué?",
  "Una vez fuera, olvídate de quién eres.",
  "¿Sabe de dónde lo he sacado?",
  "¿ De dónde la ha sacado?",
]

more_4 = [
  "Descuide, mi comisario, que la Candelaria se encarga de todo.",
  "Y no se le ocurra meterla en ninguno de sus líos.",
  "Mire, no me fío ni un pelo de ninguna de las dos, así que las tendré vigiladas bien de cerca.",
  "Como me entere de algo extraño, me las llevo a comisaría y de allí no las saca ni el Sursum corda.",
  "Y al calabozo me las llevo como me entere de algo extraño.",
  "Lo tengo todo el día en la chepa pegado, pero, anda, mi alma, entra para dentro, voy a ver si te instalo allí en uno de los cuartos del fondo.",
  "Y como ustedes pueden ver, está un poco pachucha, así que me la dejan tranquila.",
  "Como vuelvan a hablarse de la puta guerra en esta santa casa, los pongo a todos en la calle y les tiro las maletas por el balcón.",
  "Niña, tienes que comer, coger fuerzas, salir a la calle, el runrún de poco sirve.",
  "Ve por unas toallas o por algo para secar esto.",
  "Por nada.",
  "¿Cuántas veces te he dicho que no entres a limpiar en mi habitación, que de eso me encargo yo?",
  "Si quiere abroncar a alguien, aquí me tiene.",
  "Que de eso ya no hay.",
  "No voy a poner la cabeza de ninguna de mis clientas en manos de una desconocida.",
  "Ah, ¿es por eso?",
  "Venga, se le pierde el tiempo a otra.",
  "No sufra, Herminia, que entre todos hacemos una colecta para que vaya corriendo a calentarlos.",
  "Que el rojo le tenga que sacar punta a todo.",
  "¿Y cuánto me cobrarías a mí por uno como ese?",
  "Si te encuentras con alguien, arrastra los pies como si fueras una vieja.",
  "Si nadie me viene con algo evidente, no voy a investigar de dónde ha sacado el dinero para pagar todo esto.",
  "Señorita Quiroga, soy una amiga de una de sus clientas, Frau Heinz.",
  "Se ve que hay personas que han sacado a más de uno de la zona republicana y los han embarcado hasta Tánger.",
]

more_5 = [
  "A muerte con quien gane, mi alma.",
  "Y a quien Dios se la dé, san Pedro se la bendiga.",
]

more_6 = [
  "Si tienes una cara de sublevado que no puedes con ella.",
  "Pero lo que me gustaría de verdad es verte sin él.",
  "Y a quien Dios se la dé, san Pedro se la bendiga.",
  "Andrés me pidió que le diera una, pero no sabía qué quería hacer con ella.",
  "Mire, a mí me rompe el corazón no estar con mi madre, pero yo sé que tengo que solucionar mis problemas y no huir de ellos.",
]
def test_pron_ablativo():
  #sentences = pron_ablativo_sentences 
  sentences = more_1+more_2+more_3+more_4+more_5+more_6
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

_more_1 = [
  "Me temo que de momento no va a poder ser.",
  "Le ruego que lo disculpe, a veces se toma al pie de la letra las ordenanzas.",
  "Es la tercera falda que me cargo en una semana.",
  "A ver qué trapo me pongo ahora.",
  "No me digan que se han apuntado de voluntarias en el frente.",
  "Pues entonces, Candelaria, no se monte el cuento de la lechera.",
  "¿Y qué hacemos, nos comemos los mocos?",
  "Pues si nos pillan nos vamos las dos putitas a la cárcel o al cementerio civil.",
  "Y con esas piernas que Dios te ha dado, te digo que nos vamos a pasar desapercibidas.",
  "Que nosotras no nos vamos a liar aquí a tiros con todo el mundo.",
  "Como el sargento se entere de que has andado molestando a una pobre marroquí, te vas a comer tres días de arresto en la alcazaba como tres soles, chaval.",
  "¿ Se lo puede quitar usted misma?",
  "No estoy acostumbrada a que me desnude un desconocido.",
  "Usted tiene razón, pero no es cómo se imagina.",
  "Me temo que esta pulsera ya tiene dueño.",
]

_more_2 = [
  "Lo siento, solo pudimos salvarla a usted.",
  "Le ruego que lo disculpe, a veces se toma al pie de la letra las ordenanzas.",
  "Por fortuna para usted, el pieza de su marido o de su novio o lo que sea, dejó esta carta donde lo explica casi todo, que la abandona y que la deja con una mano delante y la otra detrás.",
  "No lo sabemos con certeza, en Brasil o en Buenos Aires.",
  "Pero dada la procedencia turbia de las joyas, yo no se lo aconsejo.",
  "No sé cómo lo hace, pero no se le escapa ninguna.",
  "Lo tengo todo el día en la chepa pegado, pero, anda, mi alma, entra para dentro, voy a ver si te instalo allí en uno de los cuartos del fondo.",
  "Ya lo hago yo.",
  "Porque a mí me lo parece.",
  "Si lo sabré yo...",
  "Y aunque lo hiciera, usted no podría pagarlo.",
  "Venga, niña, demuéstrale lo bien que lo haces.",
  "Es que con lo del alzamiento la cosa está muy rara.",
  "Yo se lo agradezco, pero la cosa no pinta bien y usted lo sabe mejor que yo.",
  "En la cena solo se hablaba de la poca suerte que ha tenido con lo de buscar trabajo.",
  "Si ya se lo dije, no están los tiempos como para conseguir dinero.",
  "¿ Se lo dije o no se lo dije?",
  "Pero si no lo digo por ti, hija.",
  "¿Y esto cómo lo has hecho, niña?",
  "Eso, lo que se ahorra en pollos se lo gasta en trapos.",
  "¡Ay, niña, que tengo cintura y no lo sabía!",
  "¿Eso lo has confeccionado tú?",
  "La tela ya la negocio yo y quien quiera los servicios de la niña, me lo dice, lo apunto y ya acordamos el precio.",
  "Mira, te lo pregunto porque tengo patrona nueva y está buscando modista.",
  "Cuando me entere, te lo cuento, ¿eh?",
  "¡Ay! Ya lo sé, ya lo sé.",
  "¿Cómo lo ha conseguido?",
  "Ya lo sé, solo que tengo miedo.",
  "Pues todavía no lo sé, pero no debe ser difícil.",
  "Lo conseguimos, niña.",
  "Más clarito no lo podías decir, reina mía.",
  "Niña, si no lo haces, lo perdemos todo.",
  "Se lo juro por lo más sagrado.",
]

_more_3 = [
  "Lo mismo me da que sea mora que cristiana.",
]

_more_4 = [
  "Aquí las preguntas las hago yo.",
  "¿De dónde lo has sacado?",
  "Pues me lo ha hecho una amiga.",
  "Y que no las aproveches como Dios manda.",
  "Y no me pregunte de dónde los he sacado porque los dos sabemos que son falsos.",
  "Pero si no son nuestras, y cuando Andrés salga de la cárcel las va a buscar.",
  "Y si sale, con decirle que las requisó la Policía, que vaya a pedirle cuentas.",
  "¿Sabe de dónde lo he sacado?",
  "¿De dónde la ha sacado?",
]
def test_pron_personales_de_objeto():
  #sentences = pron_personales_de_objeto_directo_sentences 
  #sentences = pron_personales_de_objeto_indirecto_sentences 
  sentences = _more_1+_more_2+_more_3+_more_4

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


