import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

subordinada_substantiva_sentences = [
  "Dicen que son amigos de Andrés.",
  "Estoy convencido de que no me conocen.",
  "Saben que estoy casado.",
  "No vi que los niños estaban en el jardín.",
  "Julio me avisó de que había mucho tráfico.",
  "No insistas en que tengo razón.",
  "Están seguros de que los ayudaré.",
  "Creen que somos españoles.",
  "Marga se olvidó de que venía su familia.",
  "Le convencieron de que tenían razón.",
]

def test_subordinada_substantiva():
  sentences = subordinada_substantiva_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_substantiva"]})
  display(sentences, nlp)

subordinada_adjetiva_sentences = [
  "Arnaldo, a quien te presenté ayer, vive con Tita.",
  "Mi abuela, que nació a principios del siglo xx, tiene más de cien años.",
  "No encuentro la corbata que me regalaste.",
  "Lorena, con quien estuve saliendo, es prima de Aurora.",
  "La empresa para la que trabajo es española.",
  "Polop, adonde vamos todos los veranos, es un pueblo muy animado.",
  "El acueducto de Segovia data del siglo 11, cuando los romanos dominaban España.",
  "Mis abuelos maternos, con los que viví de pequeño, eran italianos.",
  "Gante, donde nació Carlos I, está actualmente en Bélgica.",
  "Rodolfo, del que estuve enamorada hace unos años, se acaba de casar.",
]


def test_subordinada_adjetiva():
  sentences = subordinada_adjetiva_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_adjetiva"]})
  display(sentences, nlp)

subordinada_temporal_sentences = [
  "Blanca nunca baja a su perra antes de que sea de noche.",
  "Ángel siempre empezaba a comer antes de que se sentara su madre.",
  "Sonia pensaba casarse después de que encontrara empleo.",
  "Te espero en casa hasta que acabes el trabajo.",
  "Luis, espera aquí hasta que llegue Charo.",
  "Seguro que llama Julio apenas salgamos.",
  "Mándame un correo electrónico en cuanto sepas algo.",
  "Cuando éramos jóvenes, hacíamos muchas excursiones.",
  "Por favor, reserven las entradas en cuanto puedan.",
  "Siempre que voy a la playa, llueve.",
]

def test_subordinada_temporal():
  sentences = subordinada_temporal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_temporal"]})
  display(sentences, nlp)


subordinada_locativa_sentences = [
  "Podemos quedar donde te apetezca.",
  "Donde hay vida, hay esperanza.",
  "Pon estas medicinas donde no lleguen los niños.",
  "Tendremos que seguir hasta donde la encontremos.",
  "Tienes que esperarme donde yo te diga.",
  "Elias nunca está donde debe.",
  "Tuvimos que salir por donde entramos.",
  "Escóndete donde nadie te vea, Jesusín.",
  "Compro la fruta donde la compra Belén.",
  "Aparca donde encuentres sitio.",
]

def test_subordinada_locativa():
  sentences = subordinada_locativa_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_locativa"]})
  display(sentences, nlp)

subordinada_modal_sentences = [
  "Hemos repartido la herencia como nuestro padre quería.",
  "No sé por qué saco malas notas. Hago todo como tú lo haces.",
  "Hazlo de la manera que te ha dicho la profesora hoy en la clase.",
  "Andrés siempre conducía como no debía.",
  "El dependiente dijo que podíamos pagar el televisor como nosotros quisiéramos.",
  "Tendremos que abrir esa lata como podamos.",
  "Amalia vestía como le apetecía.",
  "Enrique dice las cosas como las piensa.",
  "Julia hacía siempre todo como ella quería.",
  "Prepara el arroz como a ti te guste.",
]


def test_subordinada_modal():
  sentences = subordinada_modal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_modal"]})
  display(sentences, nlp)

subordinada_comparativa_sentences = [
  "Vive tan lejos del centro como yo.",
  "No es tan complicado como parece.",
  "Hoy había en la corrida tanta gente como ayer.",
  "Luis habla inglés tan bien como su padre.",
  "En Nanjing, en verano, no hace tanto calor como yo pensaba.",
  "Tanto los estudiantes como los profesores desean resolver el problema de la Universidad.",
  "Ella gasta más dinero en un mes que yo gano en un año.",
  "Cuanto más se lo digo, menos me escucha.",
  "Ella se dedica más al cine que al estudio.",
  "Cuanto menos hablas, mejor para ti.",
]

def test_subordinada_comparativa():
  sentences = subordinada_comparativa_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_comparativa"]})
  display(sentences, nlp)

subordinada_causal_sentences = [
  "Es que le han llamado.",
  "Se han inundado las calles a causa de la lluvia.",
  "A Arturo lo despidieron por llegar siempre tarde.",
  "Como no habla mucho, la gente cree que Rafa es tímido.",
  "Me quedaré a cenar ya que insisten.",
  "Perdió la voz por gritar.",
  "El Sr. Ramírez no sacó al perro porque se quedó dormido en el sofá.",
  "Como estaba navegando en internet, me olvidé de sacar la basura.",
  "Le ha pasado algo, porque está llorando.",
  "Porque la tengo averiada.",
]

def test_subordinada_causal():
  sentences = subordinada_causal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_causal"]})
  display(sentences, nlp)

subordinada_consecutiva_sentences = [
  "Hacía mucho calor, por eso abrí todas las ventanas.",
  "Esta noche hay partido, así que no podemos quedar con Pedro.",
  "Juan está con gripe, por eso no ha venido hoy.",
  "Se hacía tarde, por lo tanto cogimos taxi.",
  "Llegó el jefe, así que empezamos a trabajar.",
  "Tengo tanta sed que me bebería toda la botella.",
  "Teníamos tan poco tiempo que no pudimos preparar las maletas.",
  "Ruperto estudia tanto que va a enfermar.",
  "Había tanta gente que no pudimos ver nada.",
  "Somos tan pocos en clase que practicamos muchísimo.",
]

def test_subordinada_consecutiva():
  sentences = subordinada_consecutiva_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_consecutiva"]})
  display(sentences, nlp)


subordinada_final_sentences = [
  "Tienes que venir a casa para que te conozcan mis padres.",
  "Tuve que llamar a Raquel para que me abriera la puerta.",
  "Cierra la ventana para que no nos vean los vecinos.",
  "Abre la ventana para que entre el aire.",
  "Llama a Víctor para que vaya preparando la cena.",
  "Llamé a Sara para que fuera a recoger las entradas.",
  "Tengo que hablar con Pedro para que venga a las cinco.",
  "Me escondí detrás de un árbol para que no me viera nadie.",
  "Julia ha ido al mercado a comprar pescado.",
  "Vinieron a Madrid para ver la final del campeonato.",
]

def test_subordinada_final():
  sentences = subordinada_final_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_final"]})
  display(sentences, nlp)

subordinada_concesiva_sentences = [
  "Aunque me llame Roberto, no le contestaré.",
  "A pesar de trabajar mucho, ganamos poco ahora.",
  "Por mucho que corráis, llegaréis tarde.",
  "Aunque hoy me he levantado tarde, tengo sueño.",
  "A pesar de jugar bien, perdieron el partido.",
  "Tengo frío a pesar de que hace sol.",
  "Aunque normalmente voy andando, hoy prefiero ir en autobús.",
  "Por más que griten, no les van a oír.",
  "Cristina siempre se cansa por poco que ande.",
  "Enrique nunca te deja el coche, por mucho que se lo pidas.",
]

def test_subordinada_concesiva():
  sentences = subordinada_concesiva_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_concesiva"]})
  display(sentences, nlp)

subordinada_condicional_sentences = [
  "¿Qué pasa si quemas un plástico?",
  "Si como poco, me pongo malo.",
  "Si hace frío, no salimos.",
  "Si fríes mucho la carne, se quema.",
  "Si no duermo bien, me siento mal.",
  "Si hace mucho frío, el agua se hiela.",
  "Ahora no tengo hambre, pero si tuviera hambre, me tomaría un bocadillo de queso.",
  "Si Borja viera menos la tele, aprobaría el curso sin problemas.",
  "¿Qué crees que haría Alberto si supiera la verdad?",
  "Si cogieran un taxi, llegarían a tiempo al aeropuerto.",
]

def test_subordinada_condicional():
  sentences = subordinada_condicional_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_condicional"]})
  display(sentences, nlp)


_sentences = subordinada_substantiva_sentences + subordinada_adjetiva_sentences + subordinada_temporal_sentences + subordinada_locativa_sentences
_sentences = _sentences + subordinada_modal_sentences + subordinada_comparativa_sentences + subordinada_causal_sentences + subordinada_consecutiva_sentences
_sentences = _sentences + subordinada_final_sentences + subordinada_concesiva_sentences + subordinada_condicional_sentences


def test_subordinada():
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["SUBORDINADA"]})
  display(_sentences, nlp)


