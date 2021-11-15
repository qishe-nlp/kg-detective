import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

adj_ohne_steigerung_sentences = [
  "Wir sollen diese Aufgabe so schnell wie möglich beenden.",
  "Deine Tochter ist so alt wie mein Sohn.",
]

def test_adj_ohne_steigerung():
  sentences = adj_ohne_steigerung_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_ohne_steigerung"]})
  display(sentences, nlp)

adj_komparativ_sentences = [
  "Das ist ein schöner Fernseher und kostet viel weniger, als man gedacht hat.",
  "Je schnelleren Fortschritt man macht, desto mehr Lust hat man zu lernen.",
  "Ab 1. Januar können wir endlich in einer größeren Wohnung wohnen.",
  "Das ist mir zu teuer. Der Preis ist ja viel höher, als ich gedacht habe.",
  "Lieber Herr Nachbar! Ich möchte Sie bitten, nach 22 Uhr das Radio leiser zu stellen.",
  "Das Kleid ist mir zu teuer. Haben Sie kein billigeres ?",
]

def test_adj_komparativ():
  sentences = adj_komparativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_komparativ"]})
  display(sentences, nlp)

adj_superlativ_sentences = [
  "Das Flugzeug fliegt am schnellsten.",
  "Der Zug ist das schnellste Verkehrsmittel.",
]

def test_adj_superlativ():
  sentences = adj_superlativ_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_superlativ"]})
  display(sentences, nlp)

adj_deklination_sentences = [
  "Fettes Fleisch darf ich nicht essen, geben Sie mir bitte mageres!",
  "Sie brauchen unbedingt eine rote Jacke.",
  "Vor dem Einkaufen soll man zuerst die Preise in verschiedenen Geschäften vergleichen.",
  "Die helle Bluse passt gut zu dem Rock.",
  "Die Zugspitze ist der höchste Berg in Deutschland.",
  "Der gestern in Berlin angekommene IC-Zug wird heute wieder abfahren.",
  "Wo kaufen Sie ein? Bei ALDI. Da gibt es immer viele günstige Sonderangebote.",
  "Am Rand der kleinen Stadt ist ein Wald.",
  "Und in dem Wald steht ein altes Haus.",
  "Eine steile Treppe führt in den Keller.",
]

def test_adj_deklination():
  sentences = adj_deklination_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_deklination"]})
  display(sentences, nlp)

adj_norminalisierte_sentences = [
  "Erzähl uns doch mal etwas Lustiges.",
  "Nicht alle Deutschen können sich Urlaub leisten.",
  "Der Eintritt für Minderjährige ist verboten.",
  "Leute, die sehr viel Geld verdienen oder haben, nennt man Reiche.",
  "Viele verlieren den Job. Die Statistik zeigt, dass es immer mehr Arbeitslose gibt.",
  "Dagmar wohnt in den USA. Sie sieht einen Verwandten in Europa nur selten.",
  "Der Moderator begrüßt die Anwesenden und stellt das Programm vor.",
  "Sie bleiben ein paar Tage im Bett. Das ist das Beste.",
  "Hast du schon das Neueste gehört?",
  "Ein Kluger will den Job gar nicht haben.",
]

def test_adj_norminalisierte():
  sentences = adj_norminalisierte_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_norminalisierte"]})
  display(sentences, nlp)


adj_ergänzung_mit_präposition_sentences = [
  "Der Lehrer ist zufrieden mit dem Erfolg der Schüler.",
  "Solange ich bei meinen Eltern wohne, bin ich von ihnen abhängig.",
  "Der Vater ist stolz auf seinen Sohn.",
  "Ich warte gespannt auf deine Antwort.",
  "Sport ist gut für die Gesundheit.",
  "Ich bin mit deinem Vorschlag einverstanden.",
]

def test_adj_ergänzung_mit_präposition():
  sentences = adj_ergänzung_mit_präposition_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_ergänzung_mit_präposition"]})
  display(sentences, nlp)

_sentences = adj_ohne_steigerung_sentences + adj_komparativ_sentences + adj_superlativ_sentences + adj_deklination_sentences
_sentences = _sentences + adj_norminalisierte_sentences + adj_ergänzung_mit_präposition_sentences


def test_adj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  display(sentences, nlp)


