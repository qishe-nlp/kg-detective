import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
import json

lang = "en"
pkg = PKG_INDICES[lang]

# read srt to json obj file
tbr_sentences = [
  "An hour's ride will take you to that beautiful spot.",
  "Tom's and Mike's birthdays are in June.",
  "- Where is your bike, Alice? - It's over there, between Eric's and Dave's.",
  "- Is Tom and Kate's mother an English teacher. - Yes, she is.",
  "- Excuse me. Is the supermarket far from here? - No, it's about 8 minutes' walk.",
  "Will you take part in the girls' long jump tomorrow afternoon?",
  "- You look so happy! - That's because an old friend of mine is coming.",
  "Li Yang is a teacher of my sister's. She and her classmates like him very much.",
  "We should try our best to help him. Anyway, he is a classmate of ours.",
  "This is the most popular music of one of the famous musicians' I have ever heard.",
]

def read_json(filename):
  data = []
  with open(filename) as f:
    data = json.load(f)
  return data


def test_noun_possessive():
  sentences = tbr_sentences 

  rules = ["noun_possessive"]
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": rules})
  write2csv(sentences, nlp, rules)


def test_tbr_gen():
  sentences = read_json('./S0405.json')
  #sentences = tbr_sentences 

  print(sentences)
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  rules = nlp.get_pipe("kg").rules
  write2csv(sentences, nlp, rules)

