import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

common = [
  "Hallo Lukas.",
  "Ich bin hier in Österreich in St. Johann.",
  "Wir haben das sehr schönes, kleines Appartement gemietet.",
  "Die Zimmer haben eine schöne Aussicht.",
  "Jeden Morgen sehe ich die Kirche von St. Johann.",
  "Die Sonne scheint.",
  "Wir gehen jeden Tag Ski fahren. Und jetzt haben wir Hunger!",
  "Kauf bitte zwei Liter Milch.",
  "Das ist ein Hund. Der Hund heißt Toby.",
  "Die Hauptstadt von Deutschland ist Berlin",
]

art_bestimmer_sentences = common + [
]



def test_art_bestimmer():
  sentences = art_bestimmer_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_bestimmer"]})
  display(sentences, nlp)

art_unbestimmer_sentences = common + [
]


def test_art_unbestimmer():
  sentences = art_unbestimmer_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_unbestimmer"]})
  display(sentences, nlp)

art_null_sentences = common + [
]


def test_art_null():
  sentences = art_null_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_null"]})
  display(sentences, nlp)

art_possessiv_sentences = [
  "Jetzt muss ich aber los, mein Chef ist immer pünktlich.",
  "Moment mal, wo ist meine Tasche? Ah, hier.",
  "Ich finde meine Tasche nicht. Weißt du, wo sie ist?",
  "Los, Toby, hol dir deinen Ball!",
  "Kinder, wir fahren jetzt. Zieht bitte eure Schuhe an.",
  "Entschuldigen Sie, darf ich Ihre Tasche wegstellen?",
  "Wir kommen gleich, wir müssen nur noch unsere Sachen packen.",
  "Das ist Frau Yang. Das ist ihr Büro.",
  "Hans und Anna helfen ihren Eltern oft.",
  "Ich schenke deiner Tocher ein Buch.",
]

def test_art_possessiv():
  sentences = art_possessiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_possessiv"]})
  display(sentences, nlp)

art_demostrativ_sentences = [
  "Ich begrüße Sie zum Seminar 'Geschichten erzählen'. In diesem Seminar lernen wir verschiedene Möglichkeiten kennen, wie man eine Geschichte spannend erzählen kann.",
  "Wir werden sehen, welche verschiedenen Möglichkeiten es gibt?",
  "Und einige Möglichkeiten auch selbst ausprobieren.",
  "Wir sind neun Teilnehmer und ich habe hier neun Kopien.",
  "Es ist also für jeden Teilnehmer eine Kopie da.",
  "Haben Sie Lust, dass wir nach dem Seminar alle zusammen essen gehen?",
  "In manchen Seminargruppen wollen die Leute lieber gleich nach Hause gehen.",
  "Also, diese Teilnehmer wollen essen gehen, genauer gesagt sind es sechs.",
  "Ich schlage vor, dass wir dann in das Restaurant gegenüber gehen.",
  "Oh, hier ist noch eine Jacke. Irgendein Seminarteilnehmer hat seine Jacke vergessen!",
]

def test_art_demostrativ():
  sentences = art_demostrativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["art_demostrativ"]})
  display(sentences, nlp)

def test_art():
  sentences = art_bestimmer_sentences + art_unbestimmer_sentences + art_null_sentences + art_possessiv_sentences + art_demostrativ_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ART"]})
  display(sentences, nlp)


