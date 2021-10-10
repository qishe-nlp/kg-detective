import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

adverbial_clause_of_time_sentences = [
  "When he was a child he was always trying out new ideas.",
  "As the time went on, the weather got worse.", 
  "It will be four days before they come back.",
  "I have been in Beijing since you left.",
  "As soon as I reach Canada, I will ring you up.",
]

def test_adverbial_clause_of_time():
  sentences = adverbial_clause_of_time_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_time"]})
  display(sentences, nlp)

adverbial_clause_of_reason_sentences = [
  "He is absent today, for he is ill.",
  "Since we've no money, we can't buy it.",
  "Seeing that it's raining, we'd better stay indoors.",
  "Now that you are here, you’d better stay.",
  "It must be raining, for lots of people running on the street.",
]


def test_adverbial_clause_of_reason():
  sentences = adverbial_clause_of_reason_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_reason"]})
  display(sentences, nlp)

adverbial_clause_of_comparison_sentences = [
  "He woke up as suddenly as he had fallen asleep.",
  "The youth of today are better off than we used to be.", 
  "You will be praised or blamed according as your work is good or bad.",
  "Men are happy in proportion as they are virtuous.",
  "I have no more than two pens.",
  "Jack is not more diligent than John.",
]

def test_adverbial_clause_of_comparison():
  sentences = adverbial_clause_of_comparison_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_comparison"]})
  display(sentences, nlp)


adverbial_clause_of_condition_sentences = [
  "Can tell you the truth on condition that you promise to keep a secret.",
  "You can eat ice cream on condition that you won't eat too much.",
  "Supposing it rains,shall we continue the sports meeting?",
  "Supposing anything should go wrong,what would you do then?",
  "He will sign the contract provided we offer more favorable terms.",
  "He won't be against us in the meeting provided that we ask for his advice in advance.",
  "But for the rain, we should have a pleasant journey.",
  "But for your help, we should not have finished in time.",
  "As long as you’re happy,it doesn’t matter what you do.",
  "As long as it doesn't rain, we can go.",
  "You will fail to arrive there in time unless you start earlier.",
  "If it rains tomorrow,we won’t go on a park.",
]

def test_adverbial_clause_of_condition():
  sentences = adverbial_clause_of_condition_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_condition"]})
  display(sentences, nlp)

adverbial_clause_of_concession_sentences = [
  "Although she was poor, yet she wanted to but that dress.",
  "He said he would come, he didn't, though.",
  "We'll go to travel even though the weather is bad.",
  "He'll come on time even if it rains.", 
  "Whether you believe it or not, it is true."
  "No matter what the matter may be, we should do our best.",
  "Whatever happened, he would not mind.",
]


def test_adverbial_clause_of_concession():
  sentences = adverbial_clause_of_concession_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_concession"]})
  display(sentences, nlp)

adverbial_clause_of_purpose_sentences = [
  "In order to catch up the first bus, I got up at six this morning.",
  "I'll run slowly so that you can catch up with me.", 
  "He wrote the name down for fear that/lest he should forget it.",
  "Better take more clothes in case the weather is cold.",
  "I called my professor in the hope that there could be more professional sugesstions from him.",
]


def test_adverbial_clause_of_purpose():
  sentences = adverbial_clause_of_purpose_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_purpose"]})
  display(sentences, nlp)

adverbial_clause_of_result_sentences = [
  "The wind was so strong that he could hardly move forward.",
  "It was so hot a day that they wanted to go swimming.",
  "They are such fine teachers that we all hold them in great respect.",
  "There are so many picture-story books that the boy won't leave.",
  "He gave me so little time that it was impossible for me to finish the work on time.",
]

def test_adverbial_clause_of_result():
  sentences = adverbial_clause_of_result_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adverbial_clause_of_result"]})
  display(sentences, nlp)


def test_adverbial_clause():
  sentences = adverbial_clause_of_time_sentences + adverbial_clause_of_reason_sentences + adverbial_clause_of_comparison_sentences + adverbial_clause_of_condition_sentences
  sentences = sentences + adverbial_clause_of_concession_sentences + adverbial_clause_of_purpose_sentences + adverbial_clause_of_result_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADVERBIAL_CLAUSE"]})
  display(sentences, nlp)


