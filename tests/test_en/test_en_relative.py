import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

relative_restrictive_clause_sentences = [
  "This is the bike that I lost last week.",
  "Norman Bethune was a great man who gave his life to help the Chinese people.",
  "Linda will never forget the words that her father told her.",
  "It' s a great TV program whose purpose is to bring the habit of reading back into the public.",
  "The first thing that I will do is to make a card for him.",
  "We are talking about the books and writers that we like.",
  "Who is the man that was talking to our English teacher?",
  "It's one of the best places that I have ever been to.",
  "A graduation ceremony is a custom which takes place when students graduate from a school.",
]

def test_relative_restrictive_clause():
  sentences = relative_restrictive_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["relative_restrictive_clause"]})
  display(sentences, nlp)

relative_non_restrictive_clause_sentences = [
  "John invited about 40 people to his wedding, most of whom are family members.",
  "After the flooding, people were suffering in that area, who urgently needed clean water, medicine and shelter to survive.",
  "Following the girl, we went into a hall, on whose walls hung a few pictures of some famous scientists.",
  "Edison made a lot of inventions, which I think are of great importance.",
  "I didn't become a serious climber until the fifth grade, when I went up to rescue a kite that was stuck in the branches of a tree.",
  "In 1963 the UN set up the World Food Programme, one of whose purposes is to relieve worldwide starvation.",
  "The children, all of whom had played the whole day long, were worn out.",
  "The fire, which occurred in Xinjian Village, Daxing District, was reported at 6:15 pm, according to the fire department.",
  "It is fantastic for children to have a harmonious family, where the parents treat their child like a friend.",
]


def test_relative_non_restrictive_clause():
  sentences = relative_non_restrictive_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["relative_non_restrictive_clause"]})
  display(sentences, nlp)



_sentences = relative_restrictive_clause_sentences + relative_non_restrictive_clause_sentences

def test_relative_clause():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["RELATIVE_CLAUSE"]})
  display(sentences, nlp)


