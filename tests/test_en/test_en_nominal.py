import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

nominal_subject_clause_sentences = [
  "What matters is the part we choose to act on.",
  "Whoever makes the most beautiful kite will win a prize in the Kite Festival.",
  "Whoever completes the first two stages can then choose whether to continue with one-on-one piano lessons in the final stage.",
  "It depends on hard work more than luck whether you can make your dream come true.",
  "What is known to all is that the old photographer still has to work very hard.",
  "I was going to pay by cash when it suddenly occurred to me that I had left my purse at home.",
  "There is no doubt, from my point of view, that what matters is not what happens to you, but what you remember and how you remember it.",
  "What shocked the world was that North Korea carried out its nuclear bomb test again.", 
]

def test_nominal_subject_clause():
  sentences = nominal_subject_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_subject_clause"]})
  display(sentences, nlp)

nominal_object_clause_sentences = [
  "Can you tell me if there is a restaurant on it?",
  "Do you know where Jane lives?",
  "Could you tell me where it is?",
  "Will you please show me how I can operate this new machine?", 
  "Do you know how much she paid for the iPad last week?",
  "She asked if I would go shopping with her.",
  "I'd like to know where we will go camping.",
  "Could you tell me when you will start your vacation?",
  "I don't remember where I bought the book yesterday.",
  "Could you please tell me when they will arrive tomorrow?",
  "And one of the most amazing things I've learned while traveling such a distance and diverse locations is how remarkably connected we are to each other and our planet.",
  "In the West, red, or the Red Scare, are synonymous with fear of communism, representing a major foe to the United States in red sends an immediate message to the viewer.",
  "Clear maps of neighborhoods and remote regions of the island before the quake just didn't exist, so international aid workers had no sense of space and no fast way of learning.",
  "But the Earth is a big and complex place, so traditionally, geography is studied as two interconnected parts, physical geography and human geography.",
  "The rare combination of glaciers and volcanoes not only influences the land, it also influences the water.",
]


def test_nominal_object_clause():
  sentences = nominal_object_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_object_clause"]})
  display(sentences, nlp)

nominal_predicative_clause_sentences = [
  "A paper plant is where paper is made.",
  "The question is whether we should ask them for help.",
  "The moment that Leo will never forget is when Mr.Green gave him a lot of valuable advice on how to improve his writing.",
  "What I value about my father is that he shows love and care for me and my family.",
  "The infrastructure of a country is what makes everything run smoothly.",
  "Life is what happens to you while you are busy making other plans.",
  "Yes, that's why I try my best to learn English well.",
  "The friendly atmosphere is what I like.",
  "Home is where somebody notices when you are no longer there.",
  "The question that puzzled them is how it is that they can get rid of the air pollution in the area.",
  "And one of the most amazing things I've learned while traveling such a distance and diverse locations is how remarkably connected we are to each other and our planet.",
  "Covered in ice and snow, this frigid continent has been one of the least mapped areas on Earth, and for good reason.",
  "Because anyone can update the map as spatial features change, the data is always fresh and ready to be used.",
  "Since the Great Barrier Reef, like all coral reefs, is life, the reef itself is part of the biosphere.",
  "Believe it or not, these delicate-looking coral reefs are most successful in areas where the hydrosphere and the atmosphere clash, creating lots of waves.",
]

def test_nominal_predicative_clause():
  sentences = nominal_predicative_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_predicative_clause"]})
  display(sentences, nlp)


_sentences = nominal_subject_clause_sentences + nominal_object_clause_sentences + nominal_predicative_clause_sentences

def test_nominal():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOMINAL_CLAUSE"]})
  display(sentences, nlp)


