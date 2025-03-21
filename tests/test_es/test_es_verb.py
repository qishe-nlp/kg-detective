import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

verb_condicional_compuesto_sentences = [
  "Lo siento, Luisa. Yo te habría acompañado al médico, pero no sabía nada.",
  "Estoy segura de que Luis nos habría ayudado, pero no estaba en casa.",
  "Yo habría llamado a Carla, pero no tenía su teléfono.",
  "Yo no habría acabado la carrera sin la ayuda de mi hermana.",
  "Jorge no vino con nosotros a Tánger porque no le habrían dejado sus padres.",
  "No sé. No habrían desayunado nada.",
  "Raquel no pudo estudiar porque habría estado enferma.",
  "¿Qué habría hecho usted en mi lugar?",
  "Si hubiera conocido su opinión, jamás le habría propuesto matrimonio.",
  "Habría podido decir algo antes.",
  "El otro día Gema estaba muy triste...habría tenido una pelea con su novio.",
  "Sin Jorge, no habríamos podido acabar el trabajo a tiempo la semana pasada.",
  "La fiesta estuvo bien, pero habría estado mejor con otro tipo de música.",
  "Si el problema se hubiera detectado antes, habría sido solucionado a tiempo.",
  "De haber recibido la carta, la reunión habría sido programada para ayer.",
  "Si la inversión se hubiera realizado, muchas familias habrían sido beneficiadas.",
  "Con mejores medidas de seguridad, el robo habría sido evitado.",
  "Con una mejor planificación, se habría completado el proyecto a tiempo.",
  "Si no hubiera habido retrasos, se habría publicado el libro el año pasado.",
  "Si se hubieran seguido las instrucciones, se habría logrado el objetivo.",
  "De haberse aprobado la ley, se habrían implementado nuevas medidas de seguridad.",
  "Me habría vestido más formal si lo hubiera sabido.",
  "Si tú hubieras estudiado, te habrías sentido más seguro en el examen.",
  "¿Se habrían arrepentido de su decisión si hubieran tenido más información?",
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
  "¿Le gustaría pagar menos en su factura de la luz?",
  "Querría vivir en una gran ciudad.",
  "Deberíamos respetar más a las personas mayores.",
  "Buenos días, querría dos barras de pan y un bollo.",
  "¿Sería usted tan amable de darme sus datos de contacto?",
  "Si tuviera más tiempo, haría más cosas. ",
  "Te acompañaría si me dieran el día libre.",
  "El error sería corregido si alguien lo notara.",
  "La propuesta sería aceptada si cumpliera con los requisitos.",
  "Si hubiera más presupuesto, más viviendas serían construidas.",
  "Con un mejor equipo, el trabajo sería realizado más rápido.",
  "Con mejor organización, se entregarían los informes más rápido.",
  "Con una buena estrategia, se aumentarían las ventas fácilmente.",
  "Si se diera más promoción, se venderían más boletos.",
  "Si hubiera más tiempo, se revisarían todos los documentos con calma.",
  "Yo me levantaría más temprano si no estuviera tan cansado.",
  "Nos mudaríamos a otra ciudad si tuviéramos la oportunidad.",
  "¿Se peinarían diferente si tuvieran otro tipo de cabello?",
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
  "Míreme",
  "Quédele agradecida por el detalle, porque por el momento eso la va a salvar de ir a la cárcel.",
  "Acompáñeme",
  "Apúntelo en la cuenta de las que me debe.",
  "Dile a la señora Candelaria que ya he engordado los 3 kg que me pidió.",
  "Déjanos solos, Jamila, por favor.",
  "Yo no soy la manera, créame.",
  "Escúcheme.",
  "Escúcheme bien, porque no volveré a repetirlo.",
  "Espérate que voy a dejar esto dentro y nos vamos a dar una vuelta.",
  "Venga, niña, demuéstrale lo bien que lo haces.",
  "Déjeme la revista, por favor.",
  "Apúntamelo, Rosa.",
  "Échala ahí, échala.",
  "Y dile a tu amigo que no sea tímido e invita a los siguientes.",
  "Tantear, chiquilla, tantear el terreno, tú déjame a mí.",
  "Entra, entra, chiquilla, y cuéntamelo todo, que estoy mala sin saber qué ha pasado.",
]

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

more_1 = [
  "No se preocupe, ya me encargo yo.",
  "Pero no se preocupe, porque esto también me ha llevado a creerla.",
  "No se me ahogue en un vaso de agua, señorita Quiroga, por favor, que seguro que al problema de la vivienda le encontramos remedio.",
  "Y no se le ocurra meterla en ninguno de sus líos.",
  "Señorita, no se preocupe, Jamila recoge todo esto.",
  "No te rías, Juanito, que reírse seca las entendederas.",
  "No se meta en líos.",
  "Pero tú no te desesperes, chiquilla, que algo encontraremos.",
  "Pero no se nos suba a la Parra, Candelaria.",
  "Pues entonces, Candelaria, no se monte el cuento de la lechera.",
  "Como no se meta ahoro mismo en la cama, mañana por la mañana lo primero que hago es decirle a la Benita que se está usted viendo con el practicante los viernes en la cornisa.",
  "No se preocupe, todo va a salir bien.",
  "Sí, madre, no se preocupe, que yo puedo solo.",
  "Candelaria, no se meta.",
]

more_2 = [
  "No llore, señorita.",
  "Venga, levántate, que se enfría el desayuno.",
  "¿ Sabéis lo que me han pedido por estas dos gallinas viejas?",
  "Pero bueno, Candelaria, vaya vestido fino que llevas.",
  "Venga, tira.",
]

more_3 = [
  "Disculpe.",
  "Anda, niña, sigue con el desayuno mientras yo me cambio.",
  "Pero bueno, pero bueno, no acapare usted la revista, que yo también tengo derecho.",
  "Cuando la pases, usa la carretera de Ceuta y que encontrarás de frente con la estación.",
  "Esconde el dinero.",
]
def test_verb_imperativo():
  sentences = verb_imperativo_con_pron_sentences + verb_imperativo_regulares_sentences + verb_imperativo_irregulares_sentences
  sentences = sentences + more_1 + more_2 + more_3

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_imperativo"]})
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
  "El proyecto será completado por el equipo.",
  "La casa será construida por los arquitectos.",
  "El libro será publicado el próximo año.",
  "Las cartas serán enviadas por correo.",
  "El problema será resuelto por los expertos.",
  "La cena será preparada por mi madre.",
  "Los documentos serán firmados por el director.",
  "El coche será reparado por el mecánico.",
  "Las invitaciones serán entregadas personalmente.",
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
  "El proyecto habrá sido completado para diciembre.",
  "La casa habrá sido construida antes de la primavera.",
  "El libro habrá sido publicado para el próximo mes.",
  "Las cartas habrán sido enviadas antes del viernes.",
  "El problema habrá sido resuelto para entonces.",
  "La cena habrá sido preparada antes de que lleguen los invitados.",
  "Los documentos habrán sido firmados para mañana.",
  "El coche habrá sido reparado antes del viaje.",
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
  "El libro es leído por muchos estudiantes.",
  "La carta es escrita por María.",
  "El pastel es preparado por mi abuela.",
  "Las manzanas son vendidas en el mercado.",
  "El coche es lavado por mi hermano.",
  "La película es dirigida por un famoso director.",
  "Los problemas son resueltos por el equipo.",
  "La casa es decorada por un diseñador profesional.",
  "Yo me levanto temprano todos los días.",
  "Tú te lavas las manos antes de comer.",
  "Él se mira en el espejo.",
  "Nosotros nos vestimos rápidamente por la mañana.",
  "Vosotros os divertís en la fiesta.",
  "Ellos se acuestan a las diez de la noche.",
  "Ella se peina antes de salir.",
  "Ustedes se relajan después del trabajo.",
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
  "El libro fue escrito por un autor famoso.",
  "La casa fue construida en 1990.",
  "El pastel fue preparado por mi madre.",
  "Las cartas fueron enviadas ayer.",
  "El problema fue resuelto por el equipo.",
  "La película fue dirigida por un cineasta reconocido.",
  "Los documentos fueron firmados por el gerente.",
  "El coche fue reparado por el mecánico.",
  "Yo me levanté temprano ayer.",
  "Tú te lavaste las manos antes de comer.",
  "Él se miró en el espejo antes de salir.",
  "Nosotros nos vestimos rápidamente por la mañana.",
  "Vosotros os divertisteis en la fiesta anoche.",
  "Ellos se acostaron tarde anoche.",
  "Ella se peinó antes de ir al trabajo.",
  "Ustedes se relajaron después del trabajo.",
  "Fue secundada por la sirvienta de la casa.",
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
  "El libro era leído por muchos estudiantes.",
  "La casa era construida por un equipo de arquitectos.",
  "El pastel era preparado por mi abuela cada domingo.",
  "Las manzanas eran vendidas en el mercado local.",
  "El coche era lavado por mi hermano todos los sábados.",
  "La película era dirigida por un famoso director.",
  "Los problemas eran resueltos por el equipo rápidamente.",
  "La casa era decorada por un diseñador profesional.",
  "Yo me levantaba temprano todos los días.",
  "Tú te lavabas las manos antes de comer.",
  "Él se miraba en el espejo antes de salir.",
  "Nosotros nos vestíamos rápidamente por la mañana.",
  "Vosotros os divertíais en las fiestas.",
  "Ellos se acostaban tarde los fines de semana.",
  "Ella se peinaba cuidadosamente antes de ir al trabajo.",
  "Ustedes se relajaban después del trabajo.",
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
  "El libro ha sido leído por muchos estudiantes.",
  "La casa ha sido vendida por sus dueños.",
  "Las cartas han sido enviadas por correo.",
  "El proyecto ha sido aprobado por el comité.",
  "La comida ha sido preparada por el chef.",
  "Yo me he levantado temprano hoy.",
  "Tú te has duchado antes de salir.",
  "Él se ha vestido rápidamente.",
  "Nosotros nos hemos reunido con amigos.",
  "Vosotros os habéis quejado del ruido.",
  "Ellos se han acostado tarde.",
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
  "El libro había sido leído por muchos estudiantes antes de que lo recomendaran.",
  "La casa había sido vendida por sus dueños antes de que la visitáramos.",
  "Las cartas habían sido enviadas por correo antes de que llegara la noticia.",
  "El proyecto había sido aprobado por el comité antes de que presentaran las quejas.",
  "La comida había sido preparada por el chef antes de que llegaran los invitados.",
  "Yo me había levantado temprano antes de que sonara el despertador.",
  "Tú te habías duchado antes de que llegaran los invitados.",
  "Él se había vestido rápidamente antes de que comenzara la reunión.",
  "Nosotros nos habíamos reunido con amigos antes de que empezara a llover.",
  "Vosotros os habíais quejado del ruido antes de que lo solucionaran.",
  "Ellos se habían acostado tarde antes de que saliera el sol.",
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

verb_reflexivo_sentences = [
  "Me llamo Andrés.",
  "Tania siempre se despide con un beso.",
  "¿A quién te pareces, a tu padre o a tu madre?",
  "Me duermo en clase de Filosofía.",
  "¿Te encuentras bien?",
  "Siempre me dejo las llaves en casa.",
  "Yo me levanto temprano.",
  "Tú te lavas las manos.",
  "Él se peina antes de salir.",
  "Yo me levantaba temprano todos los días.",
  "Tú te lavabas las manos antes de comer.",
  "Él se peinaba antes de salir.",
  "Yo me levanté temprano ayer.",
  "Tú te lavaste las manos antes de comer.",
  "Él se peinó antes de salir.",
  "Yo me levantaré temprano mañana.",
  "Tú te lavarás las manos antes de comer.",
  "Él se peinará antes de salir.",
  "Yo me levantaría temprano si tuviera que trabajar.",
  "Tú te lavarías las manos si te lo pidieran.",
  "Él se peinaría antes de salir si tuviera tiempo.",
  "Yo me he levantado temprano hoy.",
  "Tú te has lavado las manos antes de comer.",
  "Él se ha peinado antes de salir.",
  "Yo me había levantado temprano antes de que llegaras.",
  "Tú te habías lavado las manos antes de comer.",
  "Él se había peinado antes de salir.",
  "Es importante que yo me levante temprano.",
  "Es necesario que tú te laves las manos.",
  "Es bueno que él se peine antes de salir.",
  "Si yo me levantara temprano, llegaría a tiempo.",
  "Si tú te lavaras las manos, estarías más limpio.",
  "Si él se peinara antes de salir, se vería mejor.",
  "No se me ahogue en un vaso de agua, señorita Quiroga, por favor, que seguro que al problema de la vivienda le encontramos remedio.",
  "Pues esta tarde tú y yo nos vamos a dar una vuelta.",
  "Espérate que voy a dejar esto dentro y nos vamos a dar una vuelta.",
]

def test_verb_reflexivo():
  sentences = verb_reflexivo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_reflexivo"]})
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
  "Quizá nos visite mañana.",
  "Quizá nos casemos.",
  "Quizás vuelva algún día.",
  "Quizás lleguemos tarde.",
  "Tal vez vaya al concierto esta noche.",
  "Tal vez tengas la gripe.",
  "Tal vez seáis felices algún día.",
  "Tal vez quieran cenar tarde.",
  "Es importante que el informe sea revisado antes de enviarlo.",
  "Es necesario que las propuestas sean aprobada por el comité.",
  "Espero que los documentos sean enviados antes del viernes.",
  "Dudo que el proyecto sea terminado a tiempo.",
  "Quiero que las reglas sean explicadas claramente a todos.",
  "Es probable que el examen sea revisado por otro profesor.",
  "Es importante que se respete la normativa.",
  "Espero que se realicen los cambios necesarios.",
  "Ojalá se construyan más parques en la ciudad.",
  "Espero que te levantes temprano para llegar a tiempo.",
  "Tal vez se acuerden de traer los documentos.",
]

sp_1 = [
  "No se preocupe, ya me encargo yo.",
  "No sufra.",
  "Pero no se preocupe, porque esto también me ha llevado a creerla.",
  "No se me ahogue en un vaso de agua, señorita Quiroga, por favor, que seguro que al problema de la vivienda le encontramos remedio.",
  "No me vaya a fallar, señorita.",
  "Y no se le ocurra meterla en ninguno de sus líos.",
  "Señorita, no se preocupe, Jamila recoge todo esto.",
  "No te rías, Juanito, que reírse seca las entendederas.",
  "Sagrario, no entres al trapo, que no tienen educación.",
  "A mi hermana no la llames tía vinagres, adorador de Satanás.",
  "Pues comida y ni se le ocurra dejarla en el plato.",
  "No me digas que hay alguien que se está olvidando ya de su enamorado.",
  "No diga tonterías.",
  "No se meta en líos.",
  "Pero tú no te desesperes, chiquilla, que algo encontraremos.",
  "Tú no me digas a mí que tú sabes coser.",
  "No sufra, Herminia, que entre todos hacemos una colecta para que vaya corriendo a calentarlos.",
  "No sufran, que a mí solo me ha costado la tela.",
  "Pero no se nos suba a la Parra, Candelaria.",
  "No me digan que se han apuntado de voluntarias en el frente.",
  "No me sea antiguo.",
  "Y no veas el acento que se gasta la tipa",
  "Pues entonces, Candelaria, no se monte el cuento de la lechera.",
  "Niña, tú no me digas a mí que tú sabías que ese hombre no era trigo limpio.",
  "Bueno, tampoco se quite méritos, que usted aún está de muy buen ver.",
  "No le hagas caso, está de broma.",
  "Por favor, guarde eso, no vaya a provocar una desgracia.",
  "Tú no sufras, mi alma, de eso me encargo yo.",
  "No se preocupe, todo va a salir bien.",
  "Sí, madre, no se preocupe, que yo puedo solo.",
  "No sea malpensado, comisario.",
  "Candelaria, no se meta.",
]

sp_2 = [
  "Y ahora váyase a dar una vuelta.",
  "Haya paz, haya paz.",
]

sp_3 = [
  "Que no puede ser que lleves dos semanas aquí y no hayas pisado la calle.",
]

def test_verb_subjuntivo_presente():
  sentences = verb_subjuntivo_presente_sentences + sp_1 + sp_2 + sp_3

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
  "Si trabajara desde casa, viviría en una casita en el campo.",
  "Mis jefes han sugerido que trabajáramos desde casa unos días como prueba.",
  "No creo que me cansara de la vida en el campo.",
  "Quizá teletrabajara dos días a la semana.",
  "Puede que propusiera teletrabajar solo dos días a la semana.",
  "Si el problema fuera resuelto, podríamos continuar con el plan.",
  "Me gustaría que las reglas fueran respetadas por todos.",
  "Si el paquete fuera enviado hoy, llegaría mañana.",
  "Dudaba que la propuesta fuera aceptada sin modificaciones.",
  "Ojalá que las casas fueran restauradas por el gobierno.",
  "Me gustaría que se revisara el contrato antes de firmarlo.",
  "Dudaba que se considerara la propuesta seriamente.",
  "Ojalá se invirtiera más en educación.",
  "Si se planificara mejor, habría menos problemas.",
  "Me gustaría que te callaras por un momento.",
  "Si se sintieran mejor, podrían venir a la reunión.",
  "Quisiera que nos viéramos más seguido.",
  "Ojalá se atreviera a decir lo que siente.",
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
  "Los familiares podrán ver al paciente en cuanto haya salido del quirófano.",
  "Me tranquilizaré cuando haya salido del quirófano.",
  "Me alegra que la operación haya salido bien.",
  "Espero la operación haya salido bien.",
  "¡Ojalá todo haya salido bien!",
  "Es necesario que los familiares se hayan apuntado en la lista de visitantes para pasar.",
  "No creo que haya salido ya del quirófano.",
  "Quizá hayan tenido alguna complicación.",
  "Me alegra que las quejas hayan sido atendidas rápidamente.",
  "No creo que el informe haya sido corregido todavía.",
  "Es posible que los archivos hayan sido eliminados por error.",
  "Lamento que el pago no haya sido procesado aún.",
  "Ojalá que las pruebas hayan sido evaluadas con justicia.",
  "Me alegra que se haya solucionado el problema.",
  "No creo que se hayan cumplido todas las expectativas.",
  "Ojalá se hayan corregido los errores a tiempo.",
  "Me sorprende que se haya cerrado el negocio tan rápido.",
  "Me extraña que te hayas enojado por eso.",
  "No puedo creer que se hayan despedido sin avisar.",
  "Es increíble que nos hayamos acostumbrado a este clima.",
  "Espero que te hayas recuperado pronto de la gripe.",
  "Ojalá se haya dado cuenta de su error.",
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
  "Si me hubieras avisado, habría ido contigo.",
  "Si hubieras estudiado más, habrías aprobado el examen.",
  "Si ella hubiera llegado a tiempo, no habríamos perdido el autobús.",
  "Si nosotros hubiéramos sabido antes la verdad, las cosas habrían sido diferentes.",
  "Si tú hubieras participado en el proyecto, habría tenido más éxito.",
  "Si ellos hubieran escuchado nuestras advertencias, no habría pasado nada malo.",
  "Si me hubieras avisado, habría ido contigo.",
  "Si hubieras estudiado más, habrías aprobado el examen.",
  "Si ella hubiera llegado a tiempo, no habríamos perdido el autobús.",
  "Si nosotros hubiéramos sabido antes la verdad, las cosas habrían sido diferentes.",
  "Si tú hubieras participado en el proyecto, habría tenido más éxito.",
  "Si ellos hubieran escuchado nuestras advertencias, no habría pasado nada malo.",
  "Si la decisión hubiera sido tomada antes, habríamos evitado problemas.",
  "Ojalá las cuentas hubieran sido pagadas a tiempo.",
  "Me molestó que los informes no hubieran sido entregados como se acordó.",
  "Si el plan hubiera sido ejecutado correctamente, habría funcionado mejor.",
  "Era necesario que los documentos hubieran sido revisados con más cuidado.",
  "Si se hubiera avisado antes, habríamos podido asistir.",
  "Ojalá se hubiera solucionado el inconveniente a tiempo.",
  "Me molestó que no se hubiera respetado el acuerdo.",
  "Si se hubiera investigado más, se habrían evitado errores.",
  "Si te hubieras esforzado, habrías aprobado el examen.",
  "Me habría gustado que se hubieran quedado más tiempo.",
  "Ojalá nos hubiéramos reído más en la reunión.",
  "Si te hubieras vestido mejor, habrías causado una mejor impresión.",
  "Me sorprendió que se hubieran reconciliado tan rápido.",
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
  "El libro es leído por María.",
  "Las cartas son escritas por el profesor.",
  "El libro era leído por María.",
  "Las cartas eran escritas por el profesor.",
  "El libro fue leído por María.",
  "Las cartas fueron escritas por el profesor.",
  "El libro será leído por María.",
  "Las cartas serán escritas por el profesor.",
  "El libro sería leído por María.",
  "Las cartas serían escritas por el profesor.",
  "El libro ha sido leído por María.",
  "Las cartas han sido escritas por el profesor.",
  "El libro había sido leído por María.",
  "Las cartas habían sido escritas por el profesor.",
  "Es posible que el libro sea leído por María.",
  "Es probable que las cartas sean escritas por el profesor.",
  "Si el libro fuera leído por María, sería interesante.",
  "Si las cartas fueran escritas por el profesor, serían más formales.",
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
_sentences = _sentences + verb_participio_sentences + verb_reflexivo_sentences + verb_subjuntivo_presente_sentences + verb_subjuntivo_pretérito_imperfecto_sentences
_sentences = _sentences + verb_subjuntivo_pretérito_perfecto_sentences + verb_subjuntivo_pretérito_pluscuamperfecto_sentences + verb_voz_pasiva_sentences
 

def test_verb():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["VERB"]})
  display(sentences, nlp)


