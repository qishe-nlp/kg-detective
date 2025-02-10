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
  "I'm so excited to embark with you on this journey around the world to explore the ins and outs of everything above and below the surface of the Earth over the next year.",
  "But it looks weird to us, or at least to me, because we're used to maps that tell us something about the physical space that countries and continents take up.",
  "Other cartographers tried something different with a fuller projection that unfolds the Earth and ends up with a completely different orientation without distorting anything.",
  "But cyclones bring cooler water into these shallow ecosystems, and can clean up the reef by whisking away sediment that is built up over time.",
  "Let's take a closer look at that last factoid I threw out, and go a little bananas.",
  "To look just at Guatemala, we'd jump between 13°45' and 17°48' North Latitude, and 88°14' and 92°13' West Longitude.",
  "It's all about how things vary from place to place and asking, why here?",
  "But we also know that when we tell a story, we make certain assumptions or we have to leave out facts to make sure there's a beginning, middle and end in a 10 minute video.",
  "From espressos and cappuccinos to cafe au lait and plain black, there's a coffee out there for almost everyone.",
  "Like, when you search map on the internet, this world map is one of the first that comes up.",
  "We might accidentally imply some areas have a closer population density while others are more spread out.",
  "Our last thematic map for today is a cartogram map, which uses size to compare data, like population density, regardless of the actual space these regions take up on the Earth's surface.",
  "But it looks weird to us, or at least to me, because we're used to maps that tell us something about the physical space that countries and continents take up.",
  "That's just the beginning, so we sketch out country borders.",
  "As you can see, with just a few map-making choices, we can actually help stir up some major nationalistic emotion.",
  "Just as all historians study events in time, based on what's going on or what's normal for a time period, all geographers study events in space.",
  "No matter the topic, we end up contextualizing places or human-environment interactions based on the space they existed.",
  "We take in spatial data from satellites, photos, radar and personal observation, and create data that allow us to locate buildings, route around traffic or physical features efficiently, and communicate the meaning communities give their spaces.",
  "For example, we often see a villainous type of cloud hanging over cities, called smog.",
  "Analysis shows that it can take just a few decades to change from colder to warmer climate patterns.",
  "It's like how nitrogen moves from being a gas in the atmosphere to a solid in the soil, instead of a one-way system, like aliens dropping gift-wrapped boxes of nitrogen from space or at least not that we know of!",
  "However, return migration can occur when a person goes back to stay in their country of origin, or citizenship like those with British passports were returned to Britain even though most of them had not lived there before.",

]

_more = [
]
def test_prep_with_verb():
  sentences = prep_with_verb_sentences
  #sentences = _more
 
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
  "As the city sprawls into the surrounding desert, it's increasing its paved, sealed surfaces, making it the fastest warming city in the US as well.",
  "This seafloor spreading pushes the seafloor away in both directions, and with it, the Earth's land masses, which meant we finally had the evidence Wegener was missing in 1912 for how the Earth's land masses were moving.",
  "In a polyculture system, it's common to have plants maturing at different times, and even a mix of plants and animals.",

]

more = [
]

def test_prep_with_noun():
  sentences = prep_with_noun_sentences
  #sentences = more
 
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


