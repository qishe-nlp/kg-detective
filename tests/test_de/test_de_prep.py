import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

prep_mit_akkusativ_sentences = [
  "Warum willst du denn ein Motorrad kaufen? Ein Fahrrad ist doch viel besser für dich.",
  "Warum geht Brigitte jetzt so oft ohne ihren Freund aus? Liebt sie ihn nicht mehr?",
  "Die neue Straße soll direkt durch den Park gehen.",
  "Ich bin gegen Experimente an Mäusen und Ratten.",
  "- Um wie viel Uhr fängt das Konzert an? - Um acht Uhr.",
  "Wir haben noch keine Karten für das Konzert.",
  "Das Konzert kostet nichts. Ihr könnt auch ohne Karten gehen.",
  "Kevin joggt morgens um den Campus.",
  "Ich trinke meinen Kaffee mit viel Milch, aber ohne Zucker.",
  "Schönes Wochenende! Bis nächsten Montag.",
]

def test_prep_mit_akkusativ():
  sentences = prep_mit_akkusativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_mit_akkusativ"]})
  display(sentences, nlp)

prep_mit_dativ_sentences = [
  "- Wo wohnt Johannes? - Er wohnt bei einer Familie in Wien.",
  "Franz ist nicht sehr aktiv. Er bleibt immer zu Hause.",
  "Cecile Zemp ist Schweizerin. Sie kommt aus Zürich.",
  "Frau Lett reist oft für ihren Job. Diesen Monat reist sie von Rom nach Paris.",
  "Herr Blume ist Architekt. Er arbeitet seit drei Jahren in München.",
  "Ich bin sehr müde. Ich möchte jetzt nach Hause gehen.",
  "Alle meine Verwandten sprechen Deutsch, außer meinem Vater.",
  "Ich fahre mit meinen Freunden in die Stadt.",
  "Sie hat auch eine schlechte Note von ihrer Lehrerin bekommen. Armes Kind!",
  "Ab nächster Woche habe ich wieder mehr Zeit.",
]

def test_prep_mit_dativ():
  sentences = prep_mit_dativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_mit_dativ"]})
  display(sentences, nlp)

prep_mit_akkusativ_order_dativ_sentences = [
  "Die Bibliothek steht vor der Buchhandlung.",
  "Wir laufen schnell ins Klassenzimmer.",
  "Die Bilder hängen an der Wand.",
  "Meine Bücher liegen auf dem Schreibtisch.",
  "Der Junge sitzt nicht gern neben der Schwester.",
  "Er hängt die Lampe über den Tisch.",
  "Die Schuhe stehen unter dem  Bett.",
  "Das Sofa steht zwischen den Stühlen.",
  "Er bringt das Fahrrad hinter das Haus.",
  "Mein Vater sitzt im Sessel.",
]

def test_prep_mit_akkusativ_order_dativ():
  sentences = prep_mit_akkusativ_order_dativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_mit_akkusativ_order_dativ"]})
  display(sentences, nlp)

prep_mit_genitiv_sentences = [
  "Der Mann bleibt wegen der Verspätung im Flughafen.",
  "- Er war nicht in der Stadt - die Polizei hat ihn außerhalb der Stadt gefunden.",
  "Ich mag keine Tiere. Ich wollte ein Fahrrad statt einer Katze zum Geburtstag bekommen.",
  "Die Party hat viel Spaß gemacht. Während der Party haben wir alle viel getrunken.",
  "Trotz meiner Hausaufgaben habe ich gestern einen Brief geschrieben.",
  "Umtausch ist innerhalb einer Woche möglich.",
  "Er erkennt wegen Kleinigkeiten das große Wichtige nicht.",
  "Sie schafft trotz guter Voraussetzung nur einen Teil.",
  "Alle Menschen innerhalb der vier Meere sind Brüder.",
  "Es geht nicht an, während der Vorlesung zu rauchen.",
]

def test_prep_mit_genitiv():
  sentences = prep_mit_genitiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_mit_genitiv"]})
  display(sentences, nlp)

prep_temporale_sentences = [
  "Von jetzt an machen wir die Arbeit zu zweit.",
  "Im Sommer fahren viele Deutsche an die Ostsee.",
  "Seit zwei Jahren leme ich hier Deutsch.",
  "Am Sonntag gehen Elke und ich in die Oper.",
  "Zu Weihnachten bekommen die Kinder viele Geschenke.",
  "Von acht bis zwölf Uhr haben wir Deutschunterricht.",
  "Sie hat irgendwann zwischen Ostem und Pfingsten Geburtstag.",
  "Bei Regen sind die Straßen nass und glatt.",
  "Der Schulbus fährt nur der innerhalb Schulzeit.",
  "Musst du in der Nacht arbeiten?",
]

def test_prep_temporale():
  sentences = prep_temporale_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_temporale"]})
  display(sentences, nlp)

def test_prep():
  sentences = prep_mit_akkusativ_sentences + prep_mit_dativ_sentences + prep_mit_akkusativ_order_dativ_sentences + prep_mit_genitiv_sentences + prep_temporale_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PREP"]})
  display(sentences, nlp)


