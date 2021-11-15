import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

prep_of_time_sentences = [
  "I was born on a cold morning in 1996.",
  "A big earthquake hit Japan on the afternoon of March 11th, 2011.",
  "The English teacher told me to get there at half past ten.",
  "We often go to the Children's Palace on Sunday.",
  "She usually gets to school at 7:30 in the morning.",
  "Can you come here on the morning of April 5?",
  "I know my mother's birthday is in June.",
  "We have been in China for three years.",
  "When will the second class begin? In two minutes.",
  "I have stayed in that country since 1995.",
]

def test_prep_of_time():
  sentences = prep_of_time_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_of_time"]})
  display(sentences, nlp)


prep_of_movement_sentences = [
  "The high-speed train between Qingdao and Beijing travels faster now.",
  "On sunny days, my grandma often reads a novel by the window.",
  "We planted some flowers in the garden yesterday.",
  "The earth goes around the sun.",
  "He just parked his car here and then hurried across the street.",
  "Frank held his breath under the water to search for his ring in the swimming pool.",
  "Judy, what's the weather like in Beijing?",
  "Go along Center Street and you'll find it.",
  "I can't see Lucy because she is behind the tree.",
  "It's on the fourth floor.",
]

def test_prep_of_movement():
  sentences = prep_of_movement_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_of_movement"]})
  display(sentences, nlp)


prep_of_manner_sentences = [
  "Our foreign teacher often goes to work by bike.",
  "We can pay money by scanning QR codes in many shops.",
  "This story is in simple English.",
  "The little girl made money by selling flowers.",
  "I made the coat with my own hands. It was made by hand, not with a machine.",
  "I study for a test by working with a group.",
  "How do you learn English so well? By chatting with my uncle in America online.",
  "How do you travel to school every day? I go by bus.",
  "How are you going to the Summer Palace? We’re going there by bike.",
  "I usually walk to school, but by bus when it rains.",
]

def test_prep_of_manner():
  sentences = prep_of_manner_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_of_manner"]})
  display(sentences, nlp)


prep_with_verb_sentences = [
  "And if you need any help, please call me at 010-5558 6390.",
  "In the world, more than 30% of schools do not provide safe drinking water for about 570 million children.",
  "He drove so fast at the turn that the car almost went off the road.",
  "I have a new model car. I got it from my dad.",
  "I will give a T-shirt to my brother as a birthday present.",
  "Mr. Wang's work goes beyond teaching, and he always thinks of the children first and takes good care of them.",
  "Ben was helping his mother when the rain began to beat heavily against the windows.",
  "To start with, I found the job boring, but soon I got used to it.",
  "I'm looking for the kids.",
  "With so much work filling my mind, I’ll almost break down.",
]

def test_prep_with_verb():
  sentences = prep_with_verb_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_with_verb"]})
  display(sentences, nlp)

prep_with_adj_sentences = [
  "His parents are proud of him.",
  "Are your teacher hard on all of you?",
  "It's bad for your eyes.",
  "It's very important for us to make a plan before a new term begins.",
  "Stephen Hawking was famous as a scientist.",
  "Who is better at playing basketball, you or your brother?",
  "China successfully launched a spacecraft on the far side of the moon, which, contrary to misunderstanding, is not always dark.",
  "It was obvious that the meeting was concerned with the housing reform and everyone present was concerned for their own interests.",
  "Mary was so surprised at what Tom had do to him.",
  "The funny cartoon 'Xiyangyang and Huitanglang' is popular with kids.",
]

def test_prep_with_adj():
  sentences = prep_with_adj_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_with_adj"]})
  display(sentences, nlp)

prep_with_noun_sentences = [
  "I have no taste for fame.",
  "Smoking has a great influence on our health.",
  "Demand for hospital services remained high.",
  "The reason for this meeting is to discuss the merger.",
  "I think your attitude towards your sister is very bad indeed.",
  "The difference between the two is very slight.",
  "Do you have a good relationship with most of your relatives?",
  "There was an almost complete lack of awareness of the issues involved.",
  "The decrease in profits is due to the bad market.",
  "What was his reaction to the news?",
]

def test_prep_with_noun():
  sentences = prep_with_noun_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["prep_with_noun"]})
  display(sentences, nlp)

_sentences = prep_of_time_sentences + prep_of_movement_sentences + prep_of_manner_sentences
_sentences = _sentences + prep_with_verb_sentences + prep_with_adj_sentences + prep_with_noun_sentences

def test_prep():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PREP"]})
  display(sentences, nlp)


