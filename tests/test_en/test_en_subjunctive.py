import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

subjunctive_present_sentences = [
  "If there were no air or water, there would be no living things on the earth.",
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
]

def test_subjunctive_past():
  sentences = subjunctive_past_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_past"]})
  display(sentences, nlp)

subjunctive_future_sentences = [
  "If there were a heavy snow next Sunday, we would go skating.",
  "If he should come here tomorrow, I would talk to him.",
]

def test_subjunctive_future():
  sentences = subjunctive_future_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_future"]})
  display(sentences, nlp)


subjunctive_inversion_in_mood_sentences = [
  "Were I Tom, I would refuse.",
  "Should it be necessary, I would go.",
  "Had it not been for the bad weather we would have arrived on time.",
]

def test_subjunctive_inversion_in_mood():
  sentences = subjunctive_inversion_in_mood_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["subjunctive_inversion_in_mood"]})
  display(sentences, nlp)


_sentences = subjunctive_present_sentences + subjunctive_past_sentences + subjunctive_future_sentences + subjunctive_inversion_in_mood_sentences

def test_subjuntive_mood():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["SUBJUNCTIVE_MOOD"]})
  display(sentences, nlp)


