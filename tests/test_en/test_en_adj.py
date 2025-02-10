import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

adj_ending_in_ing_sentences = [
  "With her son disappointing, she feels very worried.",
  "As we all know, typing is a tiring job.",
  "His frightened looks and trembling hands suggested that he was very afraid.",
  "Is he interesting?",
  "The film was disappointing.",
  "It's sometimes embarrassing when you have to ask people for money.",
  "It's really annoying when a train is late and there's no explanation.",
  "The film Harry Potter IV is very exciting.",
  "What boring films!",
  "The film KING KONG is a very moving one.",
]


adj_ending_in_ed_sentences = [
  "Laws that punish parents for their little children's actions against the laws get parents worried.",
  "Dad will be very surprised.",
  "We were very shocked when we heard the news.",
  "Dad was so exhausted when he came home from work.",
  "I was really amazed when I was offered it.",
  "When they heard the surprising news, they were surprised to look at each other.",
  "All of us were excited when we watched the exciting football match.",
  "I'm interested in computers but I'm not good at using it.",
  "Disneyland is so wonderful that no one feels bored there.",
  "The girl is little but she is not frightened of dogs.",
]

 

adj_order_sentences = [
  "The little white wooden house is as if it has not been lived in for years.",
  "This pretty little Spanish girl is Linda's cousin.",
  "Excuse me. Can I borrow your cheap blue plastic pencil box?",
  "We visited some friends, and spent the last few sunny days at the seaside.",
  "Tom is old enough to go to school.",
  "Mr. Smith bought a small black leather purse for his wife.",
  "One day they crossed the old Chinese stone bridge behind the palace.",
  "All these beautiful small red flowers are used for decorations in the house.",
  "In the dirty street, there are many small white flying plastics.",
  "The husband gave his wife all half his income in order to please her.",
]

adj_for_equal_comparisons_sentences = [
  "Music is as popular as sports.",
  "This room is twice as big as that one.",
  "I think Boonie Bears isn't as famous as Pleasant Goat.",
  "This city isn't the same as that one.",
  "Although this dish isn't so delicious as that one, it is more expensive than that one.",
  "This book isn't so expensive as that one, but as interesting as that one.",
  "This movie is just as boring as that one.",
  "He isn't as good at English as his sister.",
  "William's bag is not so heavy as mine.",
  "This is as good an example as the other is.",
]

def test_adj_for_equal_comparisons():
  sentences = adj_for_equal_comparisons_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_for_equal_comparisons"]})
  display(sentences, nlp)


adj_comparative_sentences = [
  "Would you mind giving me a smaller one?",
  "I think it's much better than the other films about youth in recent years.",
  "Mr. Smith thinks running is more popular than gymnastics.",
  "Is Lily's home farther away from school than Linda's?",
  "It's better than it used to be.",
  "The weather is getting colder and colder.",
  "The more you practice, the better you can play the violin.",
  "It is much heavier than mine.",
  "No. I feel even worse.",
  "He is better known for his plays.",
  "So if we're in St. Petersburg at 60 degrees North Latitude, our speed would be about only half that at the equator, 830 kilometers per hour or about 7 times faster than our cheetah.",
  "But on a local scale like on your local weather report, a low can also be an area where the pressure is less than in the surrounding area because there's actually slightly less air pressing down on that part of the Earth.",
  "Wind-current interactions are actually much more complicated than just winds pushing water around, and it's an area oceanographers are still trying to understand.",
  "It's denser than the continental crust but only a few kilometers thick.",
  "There can even be a moisture deficit, which is when the amount of moisture that evaporates is more than returns as precipitation.",
  "Like severe flooding out where no one lives, like in parts of Siberia, is a much less severe threat to humans, so less of a hazard than a mild flood in a densely packed city, like Jakarta.",
  "They're more likely than adults to put their hands and other objects in their mouths.",
]

more = [
]

def test_adj_comparative():
  sentences = adj_comparative_sentences
  #sentences = more
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_comparative"]})
  display(sentences, nlp)

adj_superlative_sentences = [
  "He is one of the most popular basketball players in the NBA.",
  "The nearest one is about 90 miles away.",
  "Chieng Mai has been one of the hottest tourist places for Chinese since the movie Lost in Thailand was shown.",
  "Of all the CD players in the shop, this one is the cheapest.",
  "The Changjiang River is one of the longest rivers in the world.",
  "I'm very proud that Beijing is one of the biggest cities in the world.",
  "Who do you think is the funniest actor?",
  "The Yellow River is the second longest river in our country.",
  "Chinese becomes one of the world's most important languages.",
  "Which month has the fewest days in a year?",
]

def test_adj_superlative():
  sentences = adj_superlative_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adj_superlative"]})
  display(sentences, nlp)

_sentences = adj_ending_in_ing_sentences + adj_ending_in_ed_sentences + adj_order_sentences + adj_for_equal_comparisons_sentences
_sentences = _sentences + adj_comparative_sentences + adj_superlative_sentences


def test_adj():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADJ"]})
  display(sentences, nlp)


