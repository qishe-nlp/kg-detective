import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

conj_subordinating_sentences = [
  "I am really proud of my group because we're always discussing and sharing study secrets together.",
  "I'm not sure whether the road to the mountains will be closed.",
  "Exciting, though one piece of the music wasn't played quite well.",
  "Our Chinese teacher didn't go to bed until he finished his work last night.",
  "To make your DIY work perfect, you'd better not start before you get all the tools ready.",
  "Although he was very tired, he continued working in his office.",
  "The nurse won't leave her patients unless she's sure they are all taken good care of.",
  "I looked through my test paper again and again so that I wouldn't make any mistakes.",
  "For example, there will be less air pollution if we drive less.",
]

def test_conj_subordinating():
  sentences = conj_subordinating_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["conj_subordinating"]})
  display(sentences, nlp)

conj_coordinating_sentences = [
  "I like eating fish and chicken.",
  "He can neither read nor write.",
  "We bought a present for Granny, but she didn't like it.",
  "Mother is cooking in the kitchen, while father is watching TV in the sitting room.",
  "My shoes are worn out, so I need new ones.",
  "The day is short, for it is now December.",
  "Which would you like better, tea or milk?",
  "She said she might come either Saturday or Sunday.",
  "Both Tom and Peter are found of watching TV.",
  "I may live either in a hotel or in a friend's house.",
]

def test_conj_coordinating():
  sentences = conj_coordinating_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["conj_coordinating"]})
  display(sentences, nlp)

def test_conj():
  sentences = conj_subordinating_sentences + conj_coordinating_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["CONJ"]})
  display(sentences, nlp)


