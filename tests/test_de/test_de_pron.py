import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]


pron_personal_sentences = [
  "Das ist Petra. Sie kommt aus der Schweiz.",
  "Das ist Paul. Er kommt aus Österreich.",
  "Kennst du Ainagul und Andrej? Sie eben in Kirgistan.",
  "Marilena und Katharina, wo seid ihr?",
  "Guten Tag Frau Wertenschlag. Gehen Sie auch zum Bäcker?",
  "Was schenkst du deiner Mutter? Ich schenke ihr eine Tasche.",
  "Und was schenkst du deinem Vater? - Für ihn habe ich ein Buch gekauft.",
  "Und was bekommt deine Schwester? Ich habe zwei DVD-Filme für sie.",
  "Hast du ein Geschenk für Inge und Hans? Ja, ich schenke ihnen eine Flasche Wein.",
  "Und mir, was schenkst du mir? Dir schenke ich natürlich auch etwas!",
]

def test_pron_personal():
  sentences = pron_personal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personal"]})
  display(sentences, nlp)


pron_indefinit_sentences = [
  "Hast du einen Stuhl für mich? Tut mir leid, ich habe keinen.",
  "Hast du eine Lampe für mich? Nein, ich habe kiene.",
  "Kannst du mir ein Paar Socken geben? Tut mir leid, ich habe keine.",
  "Gibst du mir bitte ein Blatt Papier? Ich habe leider keins.",
  "Kann ich bitte einen Kugelschreiber haben? Tut mir leid, ich habe keinen.",
  "Ich nehme mir ein Bonbon. Magst du auch eins? Nein, danke. Ich mag keins.",
  "Bringst du mir bitte einen Kuchen mit? Ja, gerne, was für einen magst du?",
  "Hallo! Ist da jemand?",
  "Haben Sie vielleicht ein Taschentuch für mich? Tut mir leid, ich habe keins.",
  "Sie interessieren sich also für ein neues Auto. Was für eins möchten Sie denn haben?",
]

def test_pron_indefinit():
  sentences = pron_indefinit_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_indefinit"]})
  display(sentences, nlp)

pron_possessiv_sentences = [
  "Ich finde meinen Schlüssel nicht. Hier ist deiner. Wo ist meiner?",
  "Mein Handy ist kaputt, ich kann nicht telefonieren. Hier, nimm meines.",
  "Danke, dass du meine Jacke gehalten hast. Soll ich kurz deine halten?",
]

def test_pron_possessiv():
  sentences = pron_possessiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_possessiv"]})
  display(sentences, nlp)

pron_reflexiv_sentences = [
  "Weißt du noch, wie wir uns kennengelernt haben?",
  "Natürlich. Ich war spät dran und ich musste mich beeilen. Ich bin zum Bus gelaufen. Und in diesem Bus haben wir uns kennengelernt.",
  "Ja. Aber jetzt muss ich leider los, wann sehen wir uns wieder?",
  "Morgen. Ich freue mich sehr auf dich.",
  "Lisa, beeile dich bitte, wir müssen jetzt los.",
  "Ich komme ja gleich, ich muss mir nur noch die Haare kämmen. Hast du dich schon fertig angezogen?",
  "Ja, schon lange! Soll ich mich noch einmal hinsetzen und Zeitung lesen, oder kommst du jetzt.",
  "Ich komme doch gleich, jetzt reg dich doch nicht so auf.",
  "Ich rege mich überhaupt nicht auf, ich wollte mich nur erkundigen, wie lange du noch brauchst.",
  "Ja, ist ja gut. Ich bin ja schon da. Aber, wie siehst du denn aus? Willst du dir nicht was Schickeres anziehen?",
]

def test_pron_reflexiv():
  sentences = pron_reflexiv_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_reflexiv"]})
  display(sentences, nlp)

pron_relativ_sentences = [
  "Hast du das Buch, das ich dir geschenkt habe, schon gelesen?",
  "Wo sind denn die Zeitschriften, die ich gestern gekauft habe?",
  "Gibst du mir bitte den Stift, der da auf dem Tisch liegt?",
  "Das Mädchen, das mit dem Hund spielt, wohnt neben mir.",
  "Der Computer, den ich letzte Woche gekauft habe, ist kaputt.",
  "Wann gehe wir in den Kinofilm, von dem ich dir erzählt habe?",
  "Meinst du den Film, in dem es um zwei Frauen geht, die im gleichen Haus wohnen?",
  "Ja, den meine ich. Er läuft heute um acht in dem Kino, in dem wir letztes Mal auch waren.",
  "Das ist alles, was ich weiß.",
]

def test_pron_relativ():
  sentences = pron_relativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_relativ"]})
  display(sentences, nlp)

pron_demostrativ_sentences = [
  "Gefällt dir der Rock? Ja, der gefallt mir.",
  "Kennen Sie diese Stadt? Ja diese kenne ich schon lange.",
]

def test_pron_demostrativ():
  sentences = pron_demostrativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_demostrativ"]})
  display(sentences, nlp)

_sentences = pron_personal_sentences + pron_indefinit_sentences + pron_possessiv_sentences + pron_reflexiv_sentences
_sentences = _sentences + pron_relativ_sentences + pron_demostrativ_sentences


def test_pron():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PRON"]})
  display(sentences, nlp)


