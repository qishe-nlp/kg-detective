import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

common = [
]

adv_temporal_sentences = common + [
  "Wenn sie abends nach Hause geht, hat sie sehr Rückenschmerzen.",
  "Heute Abend geht sie endlich zum Club um sich anzumelden.",
  "Ayla ärgert sich, aber dann hat sie eine andere Idee: Sie geht ins Schwimmbad und schwimmt einen Kilometer-einfach so, ohne Schwimmclub. ",
  "Wir essen jetzt.",
  "Sehen wir uns morgen.",
  "Danach komme ich zu ihnen.",
  "Manchmal geht er joggen.",
]

def test_adv_temporal():
  sentences = adv_temporal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_temporal"]})
  display(sentences, nlp)


adv_lokal_sentences = common + [
  "Als sie dorthin (=zum Club) kommt, ist niemand da: Der Schwimmclub hat geschlossen!",
  "Der Hund draußen bellt den ganzen Tag.",
  "Die Tasche habe ich überall gesucht.",
  "Die Vase steht rechts auf dem Boden.",
  "Ich habe die Schlüssel doch hier oben auf das Regal gelegt.",
  "Zum Hotel gehen Sie hier die Straße links, dann weiter geradeaus bis zur Ampel.",
]

def test_adv_lokal():
  sentences = adv_lokal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_lokal"]})
  display(sentences, nlp)

adv_modal_sentences = common + [
  "Sie schwimmt sehr gern und sie überlegt seit Tagen, ob sie Mitglied in einem Schwimmclub werden soll.",
  "Ich spiele gerne Federball.",
]

def test_adv_modal():
  sentences = adv_modal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_modal"]})
  display(sentences, nlp)

adv_grad_sentences = common + [
  "Ayla arbeitet in einem Reisebüro und sie sitzt viel am Computer.",
  "Sie nimmt sich fest vor, öfter schwimmen zu gehen.",
  "Die Aufführung hat mir sehr gefallen.",
  "Vielleicht hast du Recht.",
  "Es war leider nichts mehr frei.",
]

def test_adv_grad():
  sentences = adv_grad_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_grad"]})
  display(sentences, nlp)


adv_kasual_sentences = common + [
  "Sie hat oft Rückschmerzen. Deswegen will sie mehr Sport machen.",
  "Ich kenne den Weg nicht, deshalb brauche ich Hilfe.",
]

def test_adv_kasual():
  sentences = adv_kasual_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_kasual"]})
  display(sentences, nlp)

adv_komparation_sentences = [
  "Ich habe den Film schon öfter gesehen.",
  "Mal sehen, wer von uns am ehesten zu Hause ist.",
  "Isst du lieber Reis oder Nudeln? - Am liebsten esse ich Kartoffeln.",
]

def test_adv_komparation():
  sentences = adv_komparation_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_komparation"]})
  display(sentences, nlp)

_sentences = adv_temporal_sentences + adv_lokal_sentences + adv_modal_sentences + adv_grad_sentences
_sentences = _sentences + adv_kasual_sentences + adv_komparation_sentences


def test_adv():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADV"]})
  display(sentences, nlp)


