import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

compound_sen_sentences = [
  "The sun came out and the grass dried.",
  "Not only you are funny, but also you are witty.",
  "The first was not good, neither was the second.",
  "He did not go, nor did his brother go.",
  "On the one hand I have to work, on the other hand, I have a great many visitors.",
  "One step more and you are a dead man.",
  "Make haste, or you'll miss the train.",
  "We were coming to see you, but it rained.",
  "It is raining hard, however we have to go out.",
  "I have failed, yet I shall try again.",
  "He is not a miser, on the contrary, no one could be more generous.",
  "While I like the colour of the hat, I do not like its shape.",
  "I had a headache, so I went to bed.",
  "I don't know much about China, therefore I can't advise you about it.",
  "We believe that he will succeed, for he has talent.",
  "Jen hadn’t enjoyed the play; as a result, she didn't recommend it.",
  "We bought a present for Granny, but she didn't like it.",
  "Mother is cooking in the kitchen, while father is watching TV in the sitting room.",
  "My shoes are worn out, so I need new ones.",
  "The day is short, for it is now December.",
  "How can they sing and fly so free?",
  "The swan swam towards the prince and looked into his eyes.",
  "This cast a spell on him, and he was turned to stone.",
]

def test_compound_sen():
  sentences = compound_sen_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["compound_sen"]})
  display(sentences, nlp)

_sentences = compound_sen_sentences 

def test_compound():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["COMPOUND_SEN"]})
  display(sentences, nlp)


