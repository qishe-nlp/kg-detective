import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

subordinada_substantivo_sentences = [
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
  "Conviene que aproveches el tiempo.",
  "Me gusta que mi padre grabe mis entrenamientos y mis partidos.",
]

more = [
  "Pues nada, que he pensado que ya va a ser hora de que me busque un trabajito.",
  "Me temo que de momento no va a poder ser.",
  "Pero ¿cómo se le ocurre ponerle los grilletes?",
  "Tanto si le gusta como si no, hará lo que le pido.",
  "Descuide, mi comisario, que la Candelaria se encarga de todo.",
  "Y no se le ocurra meterla en ninguno de sus líos.",
  "Y si supieran lo que me ha costado un escándalo.",
  "Pues comida y ni se le ocurra dejarla en el plato.",
  "Trabaja en Aduanas y por la tarde se dedica a lo que todos, a comprar y vender todo lo que se pueda comprar y vender.",
  "Ni yo ni nadie que yo conozco se dedique a lo que usted insinúa.",
  "Y no se le ocurra meterla en ninguno de sus líos.",
  "Para tratar con las clientas solo hace falta decirles lo guapas y lo sanas que están, así tengan un pie en la tumba.",
  "A lo mejor no necesito dinero para conseguir lo que quiero.",
  "A lo mejor me basta hacerle una visita al comisario Vázquez y decirle que alguien en la pensión trafica con pasaportes.",
  "¿ Sabéis lo que me han pedido por estas dos gallinas viejas?",
  "No hace falta que me pague nada, con la tela ya está.",
  "Tu madre tiene lo que hay que tener.",
  "Ay, parece mentir a lo inocente que sigues siendo con los mandobles que te ha propinado la vida últimamente.",
  "Como no se meta ahoro mismo en la cama, mañana por la mañana lo primero que hago es decirle a la Benita que se está usted viendo con el practicante los viernes en la cornisa.",
  "Deja que te abrace, que vales más que el oro del Perú.",
  "Perdone que no esté más presentable, pero me acabo de despertar.",
  "No se le ocurre negármelo.",
  "Mire, a mí me rompe el corazón no estar con mi madre, pero yo sé que tengo que solucionar mis problemas y no huir de ellos.",
  "El tuerto me ha dado un soplo y mire lo que he requisado.",
]

def test_subordinada_substantivo():
  #sentences = subordinada_substantivo_sentences 
  sentences = more

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_substantivo"]})
  display(sentences, nlp)

subordinada_relativo_sentences = [
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

_more = [
  "Como no se meta ahoro mismo en la cama, mañana por la mañana lo primero que hago es decirle a la Benita que se está usted viendo con el practicante los viernes en la cornisa.",
  "No hay manera de parar la hemorragia.",
  "Así que con la que está cayendo, no creo que tengan interés en andar persiguiendo por Marruecos a una presunta ladrona.",
  "Pero por los clavos de Cristo, mi comisario, desde que empezó el alzamiento no para de venir gente buscando hospedaje, que tengo hasta colchones por los suelos.",
  "Tú vete acomodándote, yo voy a salir, que tengo unos asuntos pendientes, pero a la hora de comer me lo tienes que contar todo despacio.",
  "Y de postre melón, que este año están más dulces que un caramelo.",
  "El masón pidiendo paz.",
  "Cuanto más entretenida estés, menos tiempo de darle a la cabeza.",
  "Mira, si tienes fuerzas para ayudarme, tienes fuerzas para salir.",
  "Pues nada, que he pensado que ya va a ser hora de que me busque un trabajito.",
  "Rosa, que te estoy diciendo que esta chiquilla es una joya.",
  "Si ya se lo dije, no están los tiempos como para conseguir dinero.",
  "Esta comida del demonio me pone kilos donde no tenía.",
  "Tú coges la tela que más te guste y te haces un vestido.",
  "Palomares, yo le juro por lo más sagrado que ninguno sabía a qué se dedicaba este señor.",
  "Niña, tú no me digas a mí que tú sabías que ese hombre no era trigo limpio.",
  "Si tú y yo hemos tenido suficiente mala suerte como para vivir dos vidas enteras.",
  "Todo es sobre cuestión de hacer los contactos adecuados.",
  "¿Pero quién va a querer vacas teniendo terneras?",
  "Somos nosotras las que tenemos una mercancía para vender.",
  "Olvídate de tu taller, de traer a tu madre.",
  "Salta la tapia con cuidado de no dejar que los morros en el suelo.",
  "¿Tengo cara de haber nacido ayer?",
  "Princesa, la única manera de vencer nuestros demonios es plantarles cara.",
]

def test_subordinada_relativo():
  #sentences = subordinada_relativo_sentences 
  sentences = _more

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subordinada_relativo"]})
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

_sentences = subordinada_substantivo_sentences + subordinada_relativo_sentences

_sentences = _sentences + subordinada_temporal_sentences + subordinada_locativa_sentences
_sentences = _sentences + subordinada_modal_sentences + subordinada_comparativa_sentences + subordinada_causal_sentences + subordinada_consecutiva_sentences
_sentences = _sentences + subordinada_final_sentences + subordinada_concesiva_sentences + subordinada_condicional_sentences


def test_subordinada():
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["SUBORDINADA"]})
  display(_sentences, nlp)


