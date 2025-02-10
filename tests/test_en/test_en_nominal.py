import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

nominal_subject_clause_sentences = [
  "What matters is the part we choose to act on.",
  "Whoever makes the most beautiful kite will win a prize in the Kite Festival.",
  "Whoever completes the first two stages can then choose whether to continue with one-on-one piano lessons in the final stage.",
  "It depends on hard work more than luck whether you can make your dream come true.",
  "What is known to all is that the old photographer still has to work very hard.",
  "I was going to pay by cash when it suddenly occurred to me that I had left my purse at home.",
  "There is no doubt, from my point of view, that what matters is not what happens to you, but what you remember and how you remember it.",
  "What shocked the world was that North Korea carried out its nuclear bomb test again.", 
]

def test_nominal_subject_clause():
  sentences = nominal_subject_clause_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_subject_clause"]})
  display(sentences, nlp)

nominal_object_clause_sentences = [
  "Can you tell me if there is a restaurant on it?",
  "Do you know where Jane lives?",
  "Could you tell me where it is?",
  "Will you please show me how I can operate this new machine?", 
  "Do you know how much she paid for the iPad last week?",
  "She asked if I would go shopping with her.",
  "I'd like to know where we will go camping.",
  "Could you tell me when you will start your vacation?",
  "I don't remember where I bought the book yesterday.",
  "Could you please tell me when they will arrive tomorrow?",
  "And one of the most amazing things I've learned while traveling such a distance and diverse locations is how remarkably connected we are to each other and our planet.",
  "In the West, red, or the Red Scare, are synonymous with fear of communism, representing a major foe to the United States in red sends an immediate message to the viewer.",
  "Clear maps of neighborhoods and remote regions of the island before the quake just didn't exist, so international aid workers had no sense of space and no fast way of learning.",
  "But the Earth is a big and complex place, so traditionally, geography is studied as two interconnected parts, physical geography and human geography.",
  "The rare combination of glaciers and volcanoes not only influences the land, it also influences the water.",
  "But by shading a whole area, Choropleth maps can make things look a little too simple, which can be a problem.",
  "So looking at this map might make you feel like the Earth experienced great environmental stress in the 1980s and 1990s.",
  "A team of mappers organized people around the world to help digitize photos, which means tracing images to create 2D shapes and attaching coordinates that can be plotted on a map.",
  "We want you to learn about the history of the place you call home through resources like nativelands.ca and by engaging with your local indigenous and aboriginal nations through the websites and resources they provide.",
  "But remember, human-environment interactions are fundamental to studying geography.",
  "Puffins, skuas, and kittiwakes make Icelandic sea cliffs their summer nesting home.",
  "Even still, the usually temperate climate allows the biosphere to thrive.",
  "Describing those dynamic twists and turns helps us understand our role here, our future, and the future of the planet.",
  "Could you please tell me that they will arrive tomorrow?",
  "The oceanic crust and all the tiny sediment particles that used to be on the shore of the sea were also dragged down where they melted into magma.",
  "We're still figuring out how mantle plumes work, but one common school of thought is that they get their start at the core-mantle boundary.",
  "This tells us that the area around the city probably has a lot of urbanization.",
  "Evaluating hazards can also tell us how they've changed over time and show how the environmental and human components have become even more tightly intertwined.",
  "Tell me in the comments where our time studying physical geography has inspired you to dream about living.",
  "Using maps after the outbreak began to help establish its origin, it became clear that these UN troops sent to help with earthquake recovery were improperly disposing of human waste.",
  "These moves also told the entire region that Turkey intends to be a geopolitical player and be a major player in conflict and negotiation.",
  "Economists have pointed out that the traditional metrics can't measure quality of life or overall social and physical health of a society.",
  "Remember, in order to score high on the economic measures of development, an economy has to produce and consume a lot of stuff.",
  "It also shows us that lower-income countries often have higher rates of food insecurity, which has led to assumptions over the decades about the ability of the people there to grow food.",
  "For example, another model tells us how a city grows outward in a radial fashion from the city center or central business district.",
  "It can also tell us how we imagine our city in the future, things like how many people might live in the city or what types of industry might be there.",
  "As geographers, when we talk about space-time, we mean more that space and time are becoming one.",
]

def test_nominal_object_clause():
  sentences = nominal_object_clause_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_object_clause"]})
  display(sentences, nlp)

nominal_predicative_clause_sentences = [
  "A paper plant is where paper is made.",
  "The question is whether we should ask them for help.",
  "The moment that Leo will never forget is when Mr.Green gave him a lot of valuable advice on how to improve his writing.",
  "What I value about my father is that he shows love and care for me and my family.",
  "The infrastructure of a country is what makes everything run smoothly.",
  "Life is what happens to you while you are busy making other plans.",
  "Yes, that's why I try my best to learn English well.",
  "The friendly atmosphere is what I like.",
  "Home is where somebody notices when you are no longer there.",
  "The question that puzzled them is how it is that they can get rid of the air pollution in the area.",
  "And one of the most amazing things I've learned while traveling such a distance and diverse locations is how remarkably connected we are to each other and our planet.",
  "Covered in ice and snow, this frigid continent has been one of the least mapped areas on Earth, and for good reason.",
  "Because anyone can update the map as spatial features change, the data is always fresh and ready to be used.",
  "Since the Great Barrier Reef, like all coral reefs, is life, the reef itself is part of the biosphere.",
  "Believe it or not, these delicate-looking coral reefs are most successful in areas where the hydrosphere and the atmosphere clash, creating lots of waves.",
  "Other banana hotspots like Ecuador, Panama, and India are a bit farther away, so transportation is more expensive.",
  "With this map, the really populous countries are giant, while ones with smaller populations are teeny.",
  "It's about 7.7 million square kilometers, while India is less than half the size, with 3.28 million square kilometers.",
  "But this is your community, so you know where the place is to catch up with a neighbor, like an eclectic coffee shop or walking the sculpture park.",
  "That's her perception of that space, just like we all have our own perceptions of our individual spaces.",
  "The global effort to map Haiti was such a success because it brought together those who had technology to digitize the building boundaries and roads, and those who knew the significance of those boundaries and roads.",
  "And yet magma is also close to the surface, providing heat for geysers and hot springs.",

]

def test_nominal_predicative_clause():
  sentences = nominal_predicative_clause_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["nominal_predicative_clause"]})
  display(sentences, nlp)


_sentences = nominal_subject_clause_sentences + nominal_object_clause_sentences + nominal_predicative_clause_sentences

def test_nominal():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["NOMINAL_CLAUSE"]})
  display(sentences, nlp)


