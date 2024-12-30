import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

noun_proper_sentences = [
  "My name is Jack Smith. Please call me Mr. Smith.",
  "What's his name? Mike.",
  "December is the last month of a year.",
  "The Winter Olympics was held in Sochi, Russia in February.",
  "September 10 th is Teachers' Day.",
  "Which is the second month of the year? February.",
  "His name is Jim Smith.",
  "Teachers need to work on Teachers' Day.",
  "June 1st is Children's Day.",
  "Michael, how much do you know about the Dragon Boat Festival? People usually eat rice dumplings to remember Qu Yuan.",
]

def test_noun_proper():
  sentences = noun_proper_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_proper"]})
  display(sentences, nlp)

noun_countability_sentences = [
  "Please give me three pieces of bread to eat.",
  "Jerry has many Chinese stamps.",
  "The old man used to raise many sheep to make a living on the farm.",
  "Could you please give me some bread?",
  "Are there any fish in the picture?",
  "When l hurriedly got to the airport, the lady at the window told me that there were no seats left on that plane.",
  "How many pears do you want every week?",
  "They're Germans.",
  "Do you know how many teeth a horse has and how many feet a bee has?",
  "He only had two slices of bread for breakfast.",
]

noun_with_indefinite_art_sentences = [
  "I have a pet cat.",
  "An apple a day keeps the doctor away.",
  "Mary wants to be a good doctor when she grows up.",
  "David is an eight-year-old boy with short black hair.",
  "Some bread, an egg and a glass of milk.",
  "The young man from a European country has stayed in the room for an hour.",
  "She usually has an egg and some porridge for breakfast.",
  "He's my uncle, an English teacher.",
  "'Runing Man' is a very popular TV program in China.",
  "The family will have a good time in Shanghai Disneyland.",
]

def test_noun_with_indefinite_art():
  sentences = noun_with_indefinite_art_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_with_indefinite_art"]})
  display(sentences, nlp)

noun_with_definite_art_sentences = [
  "Qingdao is a beautiful city that lies in the east of China.",
  "The Smiths are used to living in Shanghai now.",
  "Beijing is the capital of China, it has a long history.",
  "Berlin is the capital of Germany.",
  "Who's the boy under the tree?",
  "We usually go swimming in summer. But in the summer of 2018, we didn't.",
  "Listen! Someone is playing the violin.",
  "Do you like the basketball on the desk?",
  "The photo makes me think of the trip to Shanghai last year.",
]

def test_noun_with_definite_art():
  sentences = noun_with_definite_art_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["noun_with_definite_art"]})
  display(sentences, nlp)


noun_possessive_sentences = [
  "An hour's ride will take you to that beautiful spot.",
  "Tom's and Mike's birthdays are in June.",
  "It's over there, between Eric's and Dave's.",
  "Is Tom and Kate's mother an English teacher.",
  "No, it's about 8 minutes' walk.",
  "Will you take part in the girls' long jump tomorrow afternoon?",
  "That's because an old friend of mine is coming.",
  "Li Yang is a teacher of my sister's.",
  "Anyway, he is a classmate of ours.",
  "This is the most popular music of one of the famous musicians' I have ever heard.",
]


_sentences = noun_proper_sentences + noun_countability_sentences + noun_with_indefinite_art_sentences + noun_with_definite_art_sentences + noun_possessive_sentences
def test_noun():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOUN"]})
  display(sentences, nlp)


