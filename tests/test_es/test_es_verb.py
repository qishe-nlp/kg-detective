import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

verb_condicional_compuesto_sentences = [
  "Lo siento, Luisa. Yo te habría acompañado al médico, pero no sabía nada.",
  "Estoy segura de que Luis nos habría ayudado, pero no estaba en casa.",
  "Sin Jorge, no habríamos podido acabar el trabajo a tiempo la semana pasada.",
  "Yo habría llamado a Carla, pero no tenía su teléfono.",
  "Yo no habría acabado la carrera sin la ayuda de mi hermana.",
  "Jorge no vino con nosotros a Tánger porque no le habrían dejado sus padres.",
  "No sé. No habrían desayunado nada.",
  "Raquel no pudo estudiar porque habría estado enferma.",
]

def test_verb_condicional_compuesto():
  sentences = verb_condicional_compuesto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_condicional_compuesto"]})
  display(sentences, nlp)

verb_condicional_simple_sentences = [
  "Esta tarta está buena, pero estaría mejor con nata.",
  "Aquí estamos bien, pero estaríamos mejor en la playa.",
  "Soy feliz, pero sería más feliz con un buen empleo.",
  "Tocáis bien, pero tocaríais mejor con un poco más de práctica.",
  "Ustedes viven muy bien aquí, pero creo que vivirían mejor en el campo.",
  "Yo que tú no saldría esta noche.",
  "Viene mucha gente al museo, pero vendría más si no cerráramos los domingos.",
  "¿Qué harías tú en mi lugar?",
  "Yo no diría nada.",
  "Yo tendría más cuidado.",
  "¿Cuándo dijo Marta que vendría?",
]

def test_verb_condicional_simple():
  sentences = verb_condicional_simple_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_condicional_simple"]})
  display(sentences, nlp)

verb_gerundio_sentences = [
  "Europa está cambiando mucho con el euro.",
  "¡Qué pena! Se nos están pudriendo los limones.",
  "Como Matías trabaja de noche se pasa las mañanas durmiendo.",
  "He estado corriendo.",
  "Mi amiga Charo está ahora viviendo en Guayaquil.",
  "Pepita ya estaba friendo los calamares cuando llegamos.",
  "El café estaba vacío. Solo había un hombre leyendo un periódico.",
  "Ramón está siempre echándose la siesta.",
  "Mira, hay un taxi yéndose de la planta.",
  "Siendo el jefe del grupo, tiene que asumir muchas responsabilidades.",
]

def test_verb_gerundio():
  sentences = verb_gerundio_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_gerundio"]})
  display(sentences, nlp)


verb_imperativo_con_pron_sentences = [
  "Ayúdala con las bolsas, Rafa.",
  "No toques ahora la guitarra.",
  "Tócala luego.",
  "Lávalas mañana.",
  "Léelo en la biblioteca.",
  "Dale a Juan el regalo ya, Elvira.",
  "Dile a Elisa que la quieres, Jorge.",
  "A Daniel no le regaléis dinero.",
  "Sí. Dáselo.",
  "- ¿Os lavo la ropa? - No nos la laves. Ya la lavaremos nosotros.",
  "Sí, arréglasela.",
]

def test_verb_imperativo_con_pron():
  sentences = verb_imperativo_con_pron_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_imperativo_con_pron"]})
  display(sentences, nlp)

verb_imperativo_irregulares_sentences = [
  "No hagas ruido, Fernando.",
  "Tobías, sal de aquí ahora mismo.",
  "Trae pan, José por favor.",
  "Conduce despacio, Magda.",
  "Oye esta canción, Nico.",
  "No salgas solo, Andrés.",
  "Poned la tele ya, chicos",
  "Ve a por el periódico, Mario.",
  "Camarero, traiga la cuenta, por favor.",
  "Por supuesto, id.",
]

def test_verb_imperativo_irregulares():
  sentences = verb_imperativo_irregulares_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_imperativo_irregulares"]})
  display(sentences, nlp)

verb_imperativo_regulares_sentences = [
  "Me duele la cabeza. Jaime, compra aspirinas, por favor.",
  "Pasen y esperen en la sala, por favor, señores.",
  "Vamos a aterrizar, apaguen los móviles, por favor.",
  "No comáis más.",
  "Cuidado, Valentín, no corras Frena un poco.",
  "No abras la ventana, por favor, Luis.",
  "No llore por la niña, Solé.",
  "Por favor, terminen sus compras, señores.",
  "Por favor, no usen los móviles durante la conferencia.",
  "No corráis tanto, niños.",
]

def test_verb_imperativo_regulares():
  sentences = verb_imperativo_regulares_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_imperativo_regulares"]})
  display(sentences, nlp)


verb_indicativo_futuro_sentences = [
  "Iré manana.",
  "¿Y cuándo volveréis?",
  "Te llamaré el lunes.",
  "No, la acabaremos la semana que viene.",
  "Iré cuando tenga tiempo.",
  "Pero no te preocupes; lo tendré dentro de unos días.",
  "No, la haré luego.",
  "No, pero creo que vendrá más tarde.",
  "No, se lo diré mañana.",
  "No, saldrá dentro de un rato.",
]

def test_verb_indicativo_futuro():
  sentences = verb_indicativo_futuro_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_futuro"]})
  display(sentences, nlp)

verb_indicativo_futuro_perfecto_sentences = [
  "Creo que ya habré acabado el proyecto.",
  "Creo que no habré pagado el piso hasta que me jubile.",
  "Creo que para entonces habré hablado con Julia.",
  "A esa hora ya se habrá despertado.",
  "Creo que cuando tenga cincuenta años, ya habré aprendido español.",
  "¿Crees que ya habrán llegado a Salamanca?",
  "El año que viene, por estas fechas, ya me habré jubilado.",
  "A esa hora ya habrá llegado.",
  "Para dentro de dos semanas ya habrá mejorado.",
  "Cuando venga Roberto, nosotros nos habremos ido.",
]


def test_verb_indicativo_futuro_perfecto():
  sentences = verb_indicativo_futuro_perfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_futuro_perfecto"]})
  display(sentences, nlp)

verb_indicativo_presente_sentences = [
  "Yo canto en un grupo rock y Ana y Eva tocan la guitarra.",
  "Lalo y yo no viajamos nunca en avión.",
  "¿ Habla usted español?",
  "Mis padres pasan el verano en Galicia.",
  "¿Quieres un cigarrillo?",
  "Gracias. No fumo.",
  "¿A qué hora coméis?",
  "No vemos mucho la tele.",
  "¿Cuantas horas al día veis la tele?",
  "Los leones no comen hierba.",
  "¿ Bebe usted alcohol?",
  "¿Qué periódico lees tú?",
]

def test_verb_indicativo_presente():
  sentences = verb_indicativo_presente_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_presente"]})
  display(sentences, nlp)


verb_indicativo_pretérito_sentences = [
  "Pablo y Mar se casaron hace tres meses.",
  "Yolanda y Arturo vivieron en Argentina hasta 1998.",
  "¿Qué os pasó ayer?",
  "No sonó el despertador y llegamos tarde.",
  "Alba vino a España en 2006.",
  "Unos amigos míos tuvieron un accidente el fin de semana pasado.",
  "¿Cuántos hijos tuvo la abuela de Tere?",
  "Ayer fui con Leandro a un concierto y vine tarde.",
  "¿Quién hizo la cena anoche?",
  "¿Cuánto tiempo estuvo en Colombia, Doña Leo?",
  "El año pasado hicimos un viaje por Brasil.",
]

def test_verb_indicativo_pretérito():
  sentences = verb_indicativo_pretérito_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_pretérito"]})
  display(sentences, nlp)

verb_indicativo_pretérito_imperfecto_sentences = [
  "Cuando era pequeño, siempre rezaba antes de acostarme.",
  "Cuando nos casamos, vivíamos en un piso muy pequeño y Nuria trabajaba en una empresa de informática.",
  "¿Qué hacías antes de casarte?",
  "Estudiaba Derecho.",
  "Cuando vivíamos en Ciudad de México, íbamos a Acapulco todos los veranos.",
  "¿Qué querías ser de pequeña, María?",
  "Quería ser astronauta.",
  "Hace cincuenta años, pocas familias tenían televisión en España.",
  "¿Qué hacían ustedes antes de venir a España?",
  "Éramos comerciantes.",
  "¿En qué parte de Perú vivía usted cuando se casaron?",
  "Vivía en la selva, en Iquitos.",
  "Cuando era pequeño, Ramón iba unos días a la sierra todos los años.",
  "Antes no me gustaba la fruta.",
]


def test_verb_indicativo_pretérito_imperfecto():
  sentences = verb_indicativo_pretérito_imperfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_pretérito_imperfecto"]})
  display(sentences, nlp)

verb_indicativo_pretérito_perfecto_sentences = [
  "¿Toni, has reservado mesa para cenar en Xamán?",
  "He dormido poco esta noche.",
  "Sebas se ha tomado una aspirina porque le duele la cabeza.",
  "Este fin de semana ha habido muchas muertes en la carretera.",
  "El nuevo gobierno ha prometido bajar los impuestos.",
  "Me he olvidado las llaves en la oficina.",
  "Anoche volví tarde a casa y hoy no he podido levantarme temprano.",
  "Eugenio, ¿has traído el coche?",
  "Que dos hombres han atracado una joyería.",
  "La oposición ha pedido la dimisión del alcalde.",
]

def test_verb_indicativo_pretérito_perfecto():
  sentences = verb_indicativo_pretérito_perfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_pretérito_perfecto"]})
  display(sentences, nlp)


verb_indicativo_pretérito_pluscuamperfecto_sentences = [
  "Cuando llegué a la oficina, la reunión había acabado.",
  "Cuando llegamos al aeropuerto, el avión se había ido.",
  "Cuando llegaron mis padres habíamos recogido toda la casa.",
  "Cuando Aurora quiso comprar comida habían cerrado todas las tiendas.",
  "Cuando llegué al cine, la película había acabado.",
  "Luisa ya había venido cuando la llamé.",
  "Cuando llegamos la película había empezado.",
  "Cuando llamé, Elisa ya se había acostado.",
]

def test_verb_indicativo_pretérito_pluscuamperfecto():
  sentences = verb_indicativo_pretérito_pluscuamperfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_indicativo_pretérito_pluscuamperfecto"]})
  display(sentences, nlp)

verb_infinitivo_sentences = [
  "¿Cuándo empiezas a estudiar informática?",
  "¿Quieren tomar algo?",
  "Julia y Arturo vienen a cenar esta noche.",
  "Mis padres me ayudan a pagar el piso.",
  "¿Puedes venir aquí un momento, por favor?",
  "Prefiero reservar las entradas yo mismo.",
  "Cuando era pequeño, Tomás soñaba con ser bombero.",
  "¿Por qué no me enseñas a nadar?",
  "¿Saben hablar español?",
  "Fidel va a pescar en un lago casi todos los domingos.",
]


def test_verb_infinitivo():
  sentences = verb_infinitivo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_infinitivo"]})
  display(sentences, nlp)

verb_oraciones_impersonales_sentences = [
  "¿Por qué hace tanto frío?",
  "No salí porque era aún un poco pronto.",
  "Parece que hoy no hace viento.",
  "Ya hace dos meses que no voy a la piscina.",
  "En una gran empresa hay muchas oportunidades para ascender.",
  "Hoy está un poco nublado.",
  "¿Cuánto tiempo hace que no nos veíamos?",
  "¿Es de día ya?",
  "No, todavía es de noche.",
  "Hoy hay muchas nubes. Va a llover.",
  "Hay que dormir bien.",
]

def test_verb_oraciones_impersonales():
  sentences = verb_oraciones_impersonales_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_oraciones_impersonales"]})
  display(sentences, nlp)


verb_participio_sentences = [
  "Juan ya ha visto esa película dos veces.",
  "Me gustan los libros encuadernados en tela.",
  "A mis hijos les encanta la carne asada.",
  "Mis amigos estaban sentados en el césped.",
  "El Ayuntamiento ha cerrado una discoteca.",
  "Mis padres han vuelto ya de Canarias.",
  "Yo siempre compro papel reciclado.",
  "Raquel tiene ya muchas canciones bajadas de internet.",
  "Muchos árboles han muerto a causa de la lluvia ácida.",
  "Cada vez llegan más productos hechos en China.",
]

def test_verb_participio():
  sentences = verb_participio_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_participio"]})
  display(sentences, nlp)

verb_reflexivos_sentences = [
  "Me llamo Andrés.",
  "Tania siempre se despide con un beso.",
  "¿A quién te pareces, a tu padre o a tu madre?",
  "Me duermo en clase de Filosofía.",
  "¿Te encuentras bien?",
  "Siempre me dejo las llaves en casa.",
]


def test_verb_reflexivos():
  sentences = verb_reflexivos_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_reflexivos"]})
  display(sentences, nlp)

verb_subjuntivo_presente_sentences = [
  "¡Ojalá ya estén mis padres en casa!",
  "Espero que me escriban cuando lleguen a Santo Domingo.",
  "Ha llamado Lolita. Quiere que comamos fuera el domingo.",
  "¡Ojalá que la enfermedad de Alberto no sea grave!",
  "¡Ojalá que el banco nos dé el préstamo!",
  "¡Que te vaya bien en tu nuevo empleo, Nuria!",
  "Espero que entienda las instrucciones.",
  "¡Ojalá no aparezcan los López por la cena!",
  "Quiero que Raúl me consiga entradas para su próximo concierto.",
  "¡Ojalá no me pida Mariela el coche para el fin de semana!",
]

def test_verb_subjuntivo_presente():
  sentences = verb_subjuntivo_presente_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_subjuntivo_presente"]})
  display(sentences, nlp)


verb_subjuntivo_pretérito_imperfecto_sentences = [
  "Cuando era pequeño mis padres querían que jugara al tenis.",
  "Preferiría que lo lavaras en otro momento.",
  "Esperaba que llegarais más tarde.",
  "No era necesario que compraras nada.",
  "Era imposible que no se enterara nadie.",
  "No era lógico que Nadal perdiera el partido.",
  "No era difícil que ella tradujera el texto.",
  "Era normal que muriera el perro.",
  "Sería difícil que el niño apagara la televisión.",
  "Sería raro que hiciera Luis la paella.",
]

def test_verb_subjuntivo_pretérito_imperfecto():
  sentences = verb_subjuntivo_pretérito_imperfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_subjuntivo_pretérito_imperfecto"]})
  display(sentences, nlp)

verb_subjuntivo_pretérito_perfecto_sentences = [
  "¡Ojalá haya llegado Alberto!",
  "Qué mal que haya suspendido Ángel la Historia.",
  "Está muy bien que Eduardo haya aprobado la Física.",
  "Es mucho mejor que nosotras hayamos venido en metro.",
  "¡Qué frío ha hecho! ¡Ojalá no se hayan helado mis gerañios!",
  "¡Qué pena que haya muerto Boby!",
  "Me alegro de que os hayáis sacado el carné.",
  "Es una vergüenza que Inge y Peter todavía no hayan aprendido español.",
  "¡Qué pena que no hayáis ido nunca a Perú!",
  "Dudo que Luisa haya vivido en Berlín.",
]

def test_verb_subjuntivo_pretérito_perfecto():
  sentences = verb_subjuntivo_pretérito_perfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_subjuntivo_pretérito_perfecto"]})
  display(sentences, nlp)

verb_subjuntivo_pretérito_pluscuamperfecto_sentences = [
  "No me habría importado que mis padres me hubieran ayudado con la hipoteca.",
  "Mi sueño era que os hubierais ido a vivir a la sierra y me hubierais llevado con vosotros.",
  "Nos habría gustado que Andrés hubiera visto nuestra casa de Granada.",
  "Me habría hecho ilusión que Irene hubiera bailado conmigo, pero solo bailó con su primo.",
  "Probablemente Silvio no quería que Rosa hubiera alquilado el apartamento tan pronto.",
  "Mis padres se alegraban de que mi hermano hubiera roto con su novia.",
  "No me habría agradado que Emilio hubiera sacado las entradas para el teatro sin decirme nada.",
  "Nos habría sentado mal que Jacinto no hubiera cumplido su promesa de llevar a los niños al circo.",
  "A Sandra le molestó que Javier hubiera reservado ya el hotel en Cancún sin pedirle opinión.",
  "Sinceramente, me habría molestado que hubieras invitado a tus amigos sin avisarme.",
]

def test_verb_subjuntivo_pretérito_pluscuamperfecto():
  sentences = verb_subjuntivo_pretérito_pluscuamperfecto_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_subjuntivo_pretérito_pluscuamperfecto"]})
  display(sentences, nlp)


verb_voz_pasiva_sentences = [
  "La primera edición de Canciones de Lorea fue publicada en 1927.",
  "El nuevo hospital será inaugurado el mes que viene.",
  "Esta sopa se prepara en un minuto.",
  "El invierno pasado se llevaron muchos pantalones anchos.",
  "Se mezcla el amarillo con el rojo para conseguir el naranja.",
  "Actualmente, muchos ordenadores se fabrican en China.",
  "La mayoría del petróleo venezolano se exporta a Estados Unidos.",
]

def test_verb_voz_pasiva():
  sentences = verb_voz_pasiva_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_voz_pasiva"]})
  display(sentences, nlp)


_sentences = verb_condicional_compuesto_sentences + verb_condicional_simple_sentences + verb_gerundio_sentences + verb_imperativo_con_pron_sentences
_sentences = _sentences + verb_imperativo_irregulares_sentences + verb_imperativo_regulares_sentences + verb_indicativo_futuro_sentences
_sentences = _sentences + verb_indicativo_futuro_perfecto_sentences + verb_indicativo_presente_sentences + verb_indicativo_pretérito_sentences + verb_indicativo_pretérito_imperfecto_sentences
_sentences = _sentences + verb_indicativo_pretérito_perfecto_sentences + verb_indicativo_pretérito_pluscuamperfecto_sentences + verb_infinitivo_sentences + verb_oraciones_impersonales_sentences
_sentences = _sentences + verb_participio_sentences + verb_reflexivos_sentences + verb_subjuntivo_presente_sentences + verb_subjuntivo_pretérito_imperfecto_sentences
_sentences = _sentences + verb_subjuntivo_pretérito_perfecto_sentences + verb_subjuntivo_pretérito_pluscuamperfecto_sentences + verb_voz_pasiva_sentences
 

def test_verb():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["VERB"]})
  display(sentences, nlp)


