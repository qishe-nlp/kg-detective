import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

simple_s_p_sentences = [
  "He died.",
  "Internet dating hurts.",
  "He works hard.",
  "They sat together quietly.",
  "The meeting begins at nine.",
  "The sun sets in the west.",
]

def test_simple_s_p():
  sentences = simple_s_p_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["simple_s_p"]})
  display(sentences, nlp)

simple_s_c_p_sentences = [
  "I am a student.",
  "The dog seems friendly.",
  "The rumor proved false.",
  "This matter remains a mystery.",
]

def test_simple_s_c_p():
  sentences = simple_s_c_p_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["simple_s_c_p"]})
  display(sentences, nlp)

simple_s_p_o_sentences = [
  "These children are playing basketball.",
  "She speaks Korean well.",
]

def test_simple_s_p_o():
  sentences = simple_s_p_o_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["simple_s_p_o"]})
  display(sentences, nlp)


simple_s_p_io_o_sentences = [
  "I gave him a book.",
  "Can you pass me the mirror?",
  "I will buy you a meal.", 
]

def test_simple_s_p_io_o():
  sentences = simple_s_p_io_o_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["simple_s_p_io_o"]})
  display(sentences, nlp)

simple_s_p_o_c_sentences = [
  "I found this answer wrong.",
  "You can leave the door open.",
  "We elected John our chairman.",
]


def test_simple_s_p_o_c():
  sentences = simple_s_p_o_c_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["simple_s_p_o_c"]})
  display(sentences, nlp)

def test_simple_sen():
  sentences = simple_s_p_sentences + simple_s_c_p_sentences + simple_s_p_o_sentences + simple_s_p_io_o_sentences
  sentences = sentences + simple_s_p_o_c_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["SIMPLE_SEN"]})
  display(sentences, nlp)


