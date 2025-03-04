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
  "There's a lot to cover in this series, because geography encompasses all 4.5 billion years or so of the Earth's history, and even makes predictions about our future.",
  "Geographers look to find connections between the physical processes at work on Earth's surface, and under the surface too, and how people use and interact with the Earth.",
  "And now it's time to add color.",
  "With OpenStreetMap, volunteers can look at space as a container, and use it to create images to trace buildings, parks, roads, and more to create a basic digital map.",
  "Now they could find efficient routes to points they needed to get to and engage with the topology or organization of the space.",
  "With fewer trees, the soil becomes even more vulnerable to these landslide-like events, setting the stage for even more dramatic changes to come.",
  "Even when the coral dies, the limestone remains and becomes a spot for new coral to grow and thrive.",
  "That's a lot of surface area to cover literally.",
  "So it's saturated, like a sponge full of water that can't soak up anymore unless you squeeze it out.",
  "Like in 2019 alone, we produced 371 million tons of potatoes worldwide, which is like 96 pounds of potatoes per person.",
  "In fact, we can predict our impact on the environment with a formula that uses population size, how affluent a society is, which is usually measured by how much it consumes and how much access to technology it has, which can be both positive and negative.",
  "Some of these mysterious volcanoes seem to be driven by mantle plumes, which are special features that can be hundreds of kilometers across, where abnormally hot magma can rise up through the mantle and melt crustal rock into more magma.",
  "a broad, rounded dome with gentle slopes that looks like a warrior's shield, which is why they're called shield volcanoes.",
  "Then it's slowed by a series of dams that supply electricity for much of Zambia and Zimbabwe.",
  "And it isn't just the routes that are interesting to geographers, but what moves along those routes and who can access those goods, even the vehicles that do the moving.",
  "Geographers look to find connections between the physical processes at work on Earth's surface, and under the surface too, and how people use and interact with the Earth.",
  "If less snow accumulates, glaciers lose more ice on their bottom edge than they can replace at the top.",
]

def test_relative_clause_rules():
  #sentences = relative_restrictive_clause_sentences + relative_non_restrictive_clause_sentences
  sentences = more

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["relative_clause"]})
  display(sentences, nlp)

_sentences = relative_restrictive_clause_sentences + relative_non_restrictive_clause_sentences

def test_relative_clause():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["RELATIVE_CLAUSE"]})
  display(sentences, nlp)


