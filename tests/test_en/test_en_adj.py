import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

adj_ending_in_ing_sentences = [
  "With her son disappointing, she feels very worried.",
  "As we all know, typing is a tiring job.",
  "Poor boy! His frightened looks and trembling hands suggested that he was very afraid.",
  "What do you think of your English teacher? Is he interesting?",
  "The film was disappointing. I expected it to be much better.",
  "It’s sometimes embarrassing when you have to ask people for money.",
  "It’s really annoying when a train is late and there’s no explanation.",
  "The film Harry Potter Ⅳ is very exciting. We all like it very much.",
  "What boring films! Let's go out for a camping trip.",
  "The film KING KONG is a very moving one. I have seen it twice already.",
]

def test_adj_with_ing_ending():
  sentences = adj_ending_in_ing_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_ending_in_ing"]})
  display(sentences, nlp)


adj_ending_in_ed_sentences = [
  "Laws that punish parents for their little children’s actions against the laws get parents worried.",
  "You sure did a great job. Dad will be very surprised.",
  "We were very shocked when we heard the news.",
  "Dad was so exhausted when he came home from work.",
  "I had never expected to get the job. I was really amazed when I was offered it.",
  "When they heard the surprising news, they were surprised to look at each other.",
  "All of us were excited when we watched the exciting football match.",
  "I’m interested in computers but I’m not good at using it.",
  "Disneyland is so wonderful that no one feels bored there.",
  "The girl is little but she is not frightened of dogs.",
]

def test_adj_with_ed_ending():
  sentences = adj_ending_in_ed_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_ending_in_ed"]})
  display(sentences, nlp)


adj_order_sentences = [
  "The little white wooden house is as if it has not been lived in for years.",
  "This pretty little Spanish girl is Linda’s cousin.",
  "Excuse me. Can I borrow your cheap blue plastic pencil box?",
  "- How was your recent visit to Qingdao? - It was great. We visited some friends, and spent the last few sunny days at the seaside.",
  "Tom is old enough to go to school.",
  "Mr. Smith bought a small black leather purse for his wife.",
  "One day they crossed the old Chinese stone bridge behind the palace.",
  "All these beautiful small red flowers are used for decorations in the house.",
  "In the dirty street, there are many small white flying plastics.",
  "The husband gave his wife all half his income in order to please her.",
]

def test_adj_order():
  sentences = adj_order_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_order"]})
  display(sentences, nlp)


adj_for_equal_comparisons_sentences = [
  "- Which do young people prefer, music or sports? - Both. Music is as popular as sports.",
  "This room is twice as big as that one.",
  "- I think Boonie Bears isn't as famous as Pleasant Goat. - I agree with you. Boonie Bears is less famous than Pleasant Goat.",
  "This city isn't the same as that one. They are different from each other.",
  "Although this dish isn't so delicious as that one, it is more expensive than that one.",
  "This book isn't so expensive as that one, but as interesting as that one.",
  "You know what? This movie is just as boring as that one. I can't stand it.",
  "He isn't as good at English as his sister. That is to say, his sister is better at English than him.",
  "William's bag is not so heavy as mine.",
  "This is as good an example as the other is.",
]

def test_adj_equal_comparisons():
  sentences = adj_for_equal_comparisons_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_for_equal_comparisons"]})
  display(sentences, nlp)


adj_comparative_sentences = [
  "The T-shirt is too big for me. Would you mind giving me a smaller one?",
  "- What do you think of the film So Young directed by Zhao Wei? - Wonderful. I think it's much better than the other films about youth in recent years.",
  "Mr. Smith thinks running is more popular than gymnastics.",
  "Is Lily's home farther away from school than Linda's?",
  "- What do you think of the traffic in our city? - It's better than it used to be, but there's still a long way to go.",
  "Winter is coming. The weather is getting colder and colder.",
  "The more you practice, the better you can play the violin.",
  "I can't carry your bag. It is much heavier than mine.",
  "- Darling, are you feeling better now? - No. I feeI even worse.",
  "Professor White has written some short stories, but he is better known for his plays.",
]

def test_adj_comparative():
  sentences = adj_comparative_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_comparative"]})
  display(sentences, nlp)

adj_superlative_sentences = [
  "- Do you know Lin Shuhao? - Yes. He is one of the most popular basketball players in the NBA.",
  "There isn't an airport near where I live. The nearest one is about 90 miles away.",
  "Chieng Mai has been one of the hottest tourist places for Chinese since the movie Lost in Thailand was shown.",
  "Of all the CD players in the shop, this one is the cheapest.",
  "The Changjiang River is one of the longest rivers in the world.",
  "I’m very proud that Beijing is one of the biggest cities in the world.",
  "- Who do you think is the funniest actor? - I think Zhao Benshan is.",
  "The Yellow River is the second longest river in our country.",
  "Chinese becomes one of the world's most important languages.",
  "- Which month has the fewest days in a year? - February.",
]

def test_adj_superlative():
  sentences = adj_superlative_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_superlative"]})
  display(sentences, nlp)

def test_adj():
  sentences = adj_ending_in_ing_sentences + adj_ending_in_ed_sentences + adj_order_sentences + adj_for_equal_comparisons_sentences
  sentences = sentences + adj_comparative_sentences + adj_superlative_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  display(sentences, nlp)


