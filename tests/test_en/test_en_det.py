import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

det_cardinal_num_sentences = [
  "There were about six hundred students in the school building during the earthquake.",
  "Please turn to page eighty and take a look at the picture on it.",
  "It's about two hundred kilometers from Nanchong to Chengdu.",
  "Lin Tao, an 8-year-old boy, was very brave and helped his classmates run out of the classroom when the earthquake happened.",
  "- When do you usually go to bed on school nights? - At around nine o'clock. It's healthy to fall asleep before 10 p.m.",
  "There are about two thousand students in the newly built school.",
  "- I think A Bite of China III is not so good as the first two. - Oh, I agree with you.",
  "- Our school is going to hold the Third Cultural Festival? - Yes. And each of us can take part in three activities.",
  "After the government carried out the two-child policy, she had a second child in her thirties.",
  "It's my sister's birthday today. She's twelve years old.",
]

def test_det_cardinal_num():
  sentences = det_cardinal_num_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["det_cardinal_num"]})
  display(sentences, nlp)


det_ordinal_num_sentences = [
  "There are twelve months in a year. December is the twelfth month of a year.",
  "Our country is nearly seventy years old. We'll celebrate its seventieth birthday on October 1, 2019 around the country.",
  "There are five people in Dale's family. They live on the ninth floor.",
  "Almost two thirds of the students in this class wear glasses, that is 60 percent of them.",
  "The number of the students in our school is about four thousand. Two thirds of them are girls.",
  "In our class three fifths of the students are girls.",
  "The headmaster's office is on the third floor.",
  "A year is divided into twelve months. September is the ninth month of the year.",
  "Li Hua is going to be an elder brother. His parents are planning to have their second child.",
  "In the Ukraine, a fifth of the population are Russian speakers.",
]

def test_det_ordinal_num():
  sentences = det_ordinal_num_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["det_ordinal_num"]})
  display(sentences, nlp)

det_art_sentences = [
  "When you visit a museum you must ask for permission before taking photographs inside it.",
  "It's not easy for Tom to find a job because he has been in prison for many years. Now he is still out of work.",
  "In communication, a smile is usually a strong sign of a friendly and open attitude.",
  "When you finish reading the book, you will have a better understanding of life.",
  "While he was investigating ways to improve the telescope, Newton made a discovery which completely changed man's understanding of color.",
  "Nokia, the world's largest mobile phone producer, is going to find a new research center in China.",
  "This book tells the life story of Smith, who left school and worked for a newspaper at the age of 18.",
  "The Jixi today is more beautiful now. Mr. Jackson said he would visit it a third time.",
  "- Of the two bags, which one do you prefer? - The bigger one. It's a most beautiful one, I think.",
  "We all sighed with relief when the plane finally landed safely.",
]

def test_det_indefinite_art():
  sentences = det_art_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["det_indefinite_art"]})
  display(sentences, nlp)

def test_det_definite_art():
  sentences = det_art_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["det_definite_art"]})
  display(sentences, nlp)

def test_det():
  sentences = det_cardinal_num_sentences + det_ordinal_num_sentences + det_art_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["DETERMINER"]})
  display(sentences, nlp)


