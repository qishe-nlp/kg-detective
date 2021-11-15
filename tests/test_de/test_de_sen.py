import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

satz_adverbial_sentences = [
  "Bevor Sie zur Sprechstunde des Professors kommen, müssen Sie sich anmelden.",
  "Sobald er in München ankam, wurde er sofort in ein Hotel gebracht.",
  "Lesen Sie die Gebrauchsanweisung sorgfältig, bevor Sie diese Maschine bedienen.",
  "Seitdem die Preise für Energie steigen, sparen die Verbraucher merklich.",
  "Wenn er in Bonn ankam, regnete es immer.",
  "Sobald der Termin feststeht, beginnen wir mit den Vorbereitungen.",
  "Solange man lebt, muss man lernen.",
  "Bevor alle Wagen das Werk verlassen, müssen alle Wagen geprüft werden.",
  "Schmiede das Eisen, solange es heiß ist.",
  "Sie will Felix den Wecker schenken, damit sie ihn nicht jeden Morgen wecken muss.",
  "Er soll den Wecker dann so weit vom Bett weg stellen, dass er aufstehen muss, wenn der Wecker klingelt.",
  "Nachdem wir zu Abend gegessen hatte, gingen wir spazieren.",
  "Sobald die Versicherung abgeschlossen wurde, tritt der Versicherungsschutz in Kraft.",
  "Während Lisa und ich Frühstück machen, reden wir natürlich die ganze Zeit.",
  "Falls der Kunde nicht zu Hause ist, lassen Sie das Paket beim Hausmeister.",
  "Obwohl wir sehr müde waren, wollten wir die Arbeit doch fertig machen.",
  "Das Kind ist zu kein, um die Frage zu beantworten.",
  "Der Ackerbau muss erweitert werden, weil sich die Weltbevölkerung rasch vermehrt.",
  "Wenn er deutlich spricht, kann ich ihn verstehen.",
  "Indem die neue Technologie eingesetzt wird, verringert man die Risiken.",
  "Wie die Ärzte festgestellt haben, essen viele Leute zu viel.",
  "Ich bin für das Radfahren, weil Radfahren gesund ist.",
  "Diese Prüfung ist viel schwerer, als ich vorher gedacht habe.",
  "Der Lehrer führt den Versuch durch, damit er den Studenten die technischen Prozesse veranschaulicht.",
  "Wir gehen spazieren oder bleiben zu Hause, je nachdem, wie das Wetter ist.",
  "Wir müssen Badesachen oder eine Wanderaiisrüstimmg mitnehmen, je nachdem, ob wir an die See oder ins Gebirge fahren.",
  "Als ich zum ersten Mal in Deutschland war, habe ich nichts verstanden.",
  "Es macht mir Spaß. Und immer wenn ich keine Lust habe zu lernen, denke ich an meine Deutschlandreisen.",
  "Die Miete ist so hoch, dass ich die Wohnung nicht nehmen kann.",
]

def test_satz_adverbial():
  sentences = satz_adverbial_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["satz_adverbial"]})
  display(sentences, nlp)

satz_relativ_sentences = [
  "Ist das Auto, das dir so gut gefällt?",
  "Ich möchte Frau Müller, die ich dir gestern vorgestellt habe, zum Abendessen einladen.",
  "Sind das die Leute, mit denen du zusammen gewohnt hast?",
  "Das ist der Mann, in den ich mich verliebt habe.",
  "Heute wollen wir über einige Probleme diskutieren, mit denen wir in Zukunft leben müssen.",
  "Alle Kinder, die ich kenne, sehen zu viel fern.",
  "Das ist Frau Kramer, bei der ich zur Untermiete gewohnt habe.",
  "Ist das nicht der Kugelschreiber, den du suchst?",
  "Das ist das Schönste, was ich bisher gehört habe.",
  "Schlagen Sie die Wörter im Wörterbuch nach, deren Bedeutung Sie nicht kennen!",
  "Das ist alles, was sie in der Schule gelernt haben.",
  "Es gibt vieles, wovon wir träumen können.",
  "Wer A sagt, muss auch B sagen.",
  "Alle Studenten, deren Studium eine Organisation bezahlt, sind Stipendiaten.",
  "Der Zug, auf dessen Ankunft ich warte, hat eine Stunde Verspätung.",
  "Wer das sagt, lügt.",
  "Das Zimmer, in dem er wohnte, war sehr alt.",
  "Der Schüler versteht nichts, was der Lehrer im Unterricht erklärt hat.",
  "Wir haben alles erreicht, wofür wir gekämpft haben.",
  "Wer zuletzt lacht, lacht am besten.",
  "Er spricht mit einer jungen Dame, deren Namen er vergessen hat.",
  "Hamburg, wo ich drei Jahre gelebt habe, ist eine Hafenstadt.",
  "Deutschland, woher viele Reisende kommen, liegt in Mitteleuropa.",
  "Du solltest alles aufschreiben, was du für die Reise vorzubereiten hast.",
  "Die Maschinet, deren Ankunft ich auf dem Flughafen erwartete, kam aus München.",
  "Der Baum, dessen Wurzeln krank waren, mussten ersetzt werden.",
  "Unser Haus steht dort, wo der hohe Baum ist.",
  "Frau Li ist nicht gekommen, woraus wir geschlossen haben, dass sie krank ist.",
  "Der Autor verwendet alte Volkslieder, was dem Stück eine lyrische Note gibt.",
  "Herr Spätler hatte eine Alarmanlage gekauft, mit der er sein Haus gegen Einbrecher schützen wollte.",
  "Die schöne Zeit, wo ich in Österreich war, habe ich sehr gut verbracht.",
  "Wen ich nicht kenne, (den) grüße ich nicht.",
  "Wem es hier nicht gefällt, der kann nach Hause kommen.",
  "Sag mal, wer ist denn das hier? Das? Das ist doch Thomas, der mit Petra befreundet war.",
  "Ach ja. Und das ist Petra, die im Unterricht immer geredet hat. Genau.",
  "Metz war sein Name. Das war doch der, der mit der Physiklehrerin verheiratet war.",
  "Ja, die beiden, die zusammen im Wohnmobil auf dem Schulparkplatz gewohnt haben.",
  "Er verlässt Dresden, wo er vier Jahre studiert hat.",
  "Das ist der Mann, dem ich geholfen habe.",
]

def test_satz_relativ():
  sentences = satz_relativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["satz_relativ"]})
  display(sentences, nlp)

satz_subjekt_sentences = [
  "Es ist möglich, dass es im Jahre 2020 auf der Erde 8 Milliarden Menschen gibt.",
  "Es ist toll, was wir in diesem Jahr erreicht haben.",
]

def test_satz_subjekt():
  sentences = satz_subjekt_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["satz_subjekt"]})
  display(sentences, nlp)


satz_objekt_sentences = [
  "Ich weiß noch nicht, ob ich dieses Jahr im Dezember wieder Urlaub bekomme.",
  "Aber ich hofft sehr, dass es klappt.",
]


def test_satz_objekt():
  sentences = satz_objekt_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["satz_objekt"]})
  display(sentences, nlp)

satz_prädikativ_sentences = [
  "Die Frage ist, ob heute er noch kommt.",
  "Sie bleibt, was sie schom immer ist.",
  "Das wichtigste ist, dass sie die Prüfung bestanden hat.",
]

def test_satz_prädikativ():
  sentences = satz_prädikativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["satz_prädikativ"]})
  display(sentences, nlp)

_sentences = satz_adverbial_sentences + satz_relativ_sentences + satz_subjekt_sentences + satz_objekt_sentences
_sentences = _sentences + satz_prädikativ_sentences


def test_nebensatz():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NEBENSATZ"]})
  display(sentences, nlp)


