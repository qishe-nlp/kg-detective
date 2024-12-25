import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

subjunctive_present_sentences = [
  "If I were him, I would watch this book.",
  "If he studied harder, he might pass the exam.",
]

def test_subjunctive_present():
  sentences = subjunctive_present_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_present"]})
  display(sentences, nlp)

subjunctive_past_sentences = [
  "If he had taken my advice, he would not have made such a mistake.",
  "If I had got there earlier, I would have met her.",
  "If he had watched this book, he would have understood it.",
]

def test_subjunctive_past():
  sentences = subjunctive_past_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_past"]})
  display(sentences, nlp)

subjunctive_future_sentences = [
  "If there were a heavy snow next Sunday, we would go skating.",
  "If he should come here tomorrow, I would talk to him.",
  "If the world should end tomorrow, he would watch this book today.",
]

def test_subjunctive_future():
  sentences = subjunctive_future_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_future"]})
  display(sentences, nlp)

_sentences = subjunctive_present_sentences + subjunctive_past_sentences + subjunctive_future_sentences

def test_subjunctive_mood():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["SUBJUNCTIVE_MOOD"]})
  display(sentences, nlp)


