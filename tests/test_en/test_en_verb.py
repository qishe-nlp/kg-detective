import spacy
from kg_detective import PKG_INDICES
from tests.lib import *
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex

lang = "en"
pkg = PKG_INDICES[lang]

infixes = (
  LIST_ELLIPSES
  + LIST_ICONS
  + [
      r"(?<=[0-9])[+\\-\\*^](?=[0-9-])",
      r"(?<=[{al}{q}])\\.(?=[{au}{q}])".format(
          al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
      ),
      r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
      # ✅ Commented out regex that splits on hyphens between letters:
      # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
      r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
  ]
)

infix_re = compile_infix_regex(infixes)

verb_passive_voice_sentences = [
  "Yes, it is being served in the dining room.",
  "A human case of H7N9 was reported in 2014 when a woman was confirmed to be infected with the bird flu virus.",
  "Oral English exams will be held in China twice a year to give more chances to the students.",
  "When you visit our town next August, a modern sports center will have been constructed, for the National Games are to be held then.",
  "The farmer said the PLA men came to rescue timely when they were being trapped in the snowstorm.",
  "The hurricane is predicted to reach the coast tomorrow morning.",
  "Later Mrs Smith decided to buy that kind of cloth because she had been told that the cloth washed very well.",
  "He has been sent to Zimbabwe as a volunteer teacher.",
  "The hard work that you do now will be repaid later in life.",
  "The new library is being built; it will be open next year.",
  "Many maps and borders represent modern geopolitical divisions that have often been decided to be decided without the consultation, permission, or recognition of the land's original inhabitants.",
  "After being absorbed into the surface, incoming radiation is eventually re-radiated by the Earth as terrestrial radiation.",
  "In the years following the Revolution, the plate tectonics theory has been fine-tuned.",
  "And that's helped us figure out some general principles of mining landscapes, which also helps us understand where to look for different types of minerals.",
  "They weren't carried along in the boats, but studied and memorized to get a better idea of the islands, waves, winds, and currents in the Pacific Ocean.",
  "On a globe, meridians aren't equally spaced, but curved together at the poles.",
  "Water that's been absorbed into the pores within the rock expands when it freezes, building up stress and causing the rock to break.",
  "On early maps of Boston, we can even see that while its financial district isn't situated in the center of the city, it was still a major part of the transportation routes for business in the area.",
  "This growth becomes problematic when people aren't treated equitably, as we learned when talking about redlining and urban renewal.",
  "In fact, their building wasn't completely finished before people moved in.",
  "Either way, this means that places aren't lost.",
  "And it's been estimated that if all countries consumed resources in the same way as the United States, we'd need four Earths.",
  "So we can have GMOs that do things the unmodified organism never could, like a potato that releases its own pesticide or a soybean that hasn't been engineered to resist fungus.",
  "It won't be finished.",
  "It will be finished.",
  "It can be done.",
]

def test_verb_passive_voice():
  sentences = verb_passive_voice_sentences 
  nlp = spacy.load(pkg)
  nlp.tokenizer.infix_finditer = infix_re.finditer
  nlp.add_pipe('kg', config={"rules": ["verb_passive_voice"]})
  display(sentences, nlp)


verb_simple_present_tense_sentences = [
  "The students of Class 5 plant trees in the park every year.",
  "Every year many foreigners come to China to learn Chinese.",
  "She often helps her classmates with their homework.",
  "I'll ring you up as soon as he arrives.",
  "If you eat too much ice-cream, you will get sick.",
  "Many city people ride their bikes to work every day.",
  "Do you know where he lives now?",
  "Tom has an English class today.",
  "If it is fine tomorrow, I will go fishing with you.",
  "Does Zhang Ming get up early every day?",
  "Geography is finding patterns and connections between places and seemingly unrelated processes, digging deeper into the stories behind facts and asking, why is this happening here?",
  "Hi, I'm Alizé Carrère, and welcome to Crash Course Geography!",
  "My own research has taken me to the far corners of the Earth to explore, study, and document these types of issues.",
]

def test_verb_simple_present_tense():
  sentences = verb_simple_present_tense_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_simple_present_tense"]})
  display(sentences, nlp)


verb_simple_past_tense_sentences = [
  "They moved to Chengdu last month.",
  "Sam, I called you yesterday, but you were not at home. Oh, I was at my aunt's.",
  "I went there when I was twelve for the Ice and Snow Festival.",
  "When I was a baby, I lived in Beijing.",
  "Could you tell me what he said at the meeting? I didn't take part in it.",
  "I called you at seven and you didn't pick up.",
  "Linda, why were you late for school yesterday? Because I woke up late.",
  "Could you please tell me where you bought the book yesterday?",
  "Excuse me, could you tell me how the accident happened? Sorry, sir. I wasn't there at that time yesterday.",
  "Could you tell me why you came late yesterday? Because my bike was broken on my way here.",
  "The people left had altogether less money that could be taxed, so over time there wasn't enough investment in the city's drainage infrastructure.",
  "Well, actually, I wasn't in New York anymore.",
  "It wasn't long before spices, produce and other cloth was moving east to west, south to north and everywhere in between all over Asia, the Mediterranean and North Africa, which some stories say took anywhere from several months to almost 10 years.",
  "Though the Middle East and North Africa wasn't the only site of significant diffusion."
  "But it wasn't until November 2020 that we'd experience the largest civil protest in history.",
  "The area wasn't even a city by the early 1950s when Brazilian leaders decided that by 1960, it would finally be the new site of the nation's capital.",
  "And that wasn't a coincidence.",
  "It was written as a sign.",
  "It wasn't completely read as a book.",
]

def test_verb_simple_past_tense():
  sentences = verb_simple_past_tense_sentences 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_simple_past_tense"]})
  display(sentences, nlp)


verb_simple_future_tense_sentences = [
  "I wonder when they will leave for Beijing. I will go to the train station to see them off when they leave.",
  "I will cook Chinese dishes for Louise tomorrow evening.",
  "Peter, what will you do next Sunday? We will visit our grandparents.",
  "He has ordered a watch online for his father and it will be sent to him before Father's Day.",
  "If it isn't fine this weekend, our spring field trip will be cancelled.",
  "There will be a talent show in ten minutes.",
  "The summer vacation will begin next week. David is coming to stay with us.",
  "We won't go bananas and get into the full geographic story of coffee, but in 2020, coffee is mostly grown in the bean belt, which is ... , oh, I'll just show you.",
  "If our sunbeam has 100 units of radiant energy, most of those units will be intercepted before we make it to the surface.",
  "8 units of energy from our sunbeam will get returned to space, while 20 units will get scattered as diffuse radiation, but persevere to reach Earth's surface.",
  "Some of that trash will get swept into regional surface currents like gyres, but some will get caught by smaller local currents and wash up on the shore without having traveled the world.",
  "And it won't be over until the cyclone is completely cut off from the warm air mass that was its source of energy and moisture.",
  "But not all areas will be affected equally by global warming and modern climate change.",
  "But it won't be our only example, because actually many of the Earth's landscapes were shaped by glaciers in some way or another millions of years ago.",
]

def test_verb_simple_future_tense():
  sentences = verb_simple_future_tense_sentences
  #sentences = _more
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_simple_future_tense"]})
  display(sentences, nlp)


verb_present_progressive_tense_sentences = [
  "She is watering the flowers in the garden.",
  "What are you doing now, Kate? I am writing an email to my friend.",
  "He is reading newspaper in the study.",
  "They keep their hands on the phones whenever they go, even while they are having meals.",
  "Someone is knocking at the door.",
  "It's too noisy here, what's going on? They are holding a party.",
  "He together with his students is practising singing by the lake.",
  "My neighbours are decorating their houses.",
  "The wonderful life in high school you look forward to is coming.",
  "I am not making the paper-cutting with it.",
  "Aren't you doing your homework?",
]

def test_verb_present_progressive_tense():
  sentences = verb_present_progressive_tense_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_present_progressive_tense"]})
  display(sentences, nlp)



verb_past_progressive_tense_sentences = [
  "I was having a walk by the river.",
  "People were sleeping when it happened that night.",
  "Oh, I was taking a shower.",
  "One of my neighbours was playing music pretty loud.",
  "Tom slipped into the house when no one was looking.",
  "Sorry, I was thinking what was happening outside.",
  "No, I was watching TV with my friend In my bedroom.",
  "He was cooking dinner at that time.",
  "I was doing yoga at that time.",
  "I had intended to buy a ticket, but it was raining.",
  "I'm sorry, what were we talking about?",
  "So poor people weren't going to use up all the resources like Malthus thought, and disaster wasn't imminent.",
]

def test_verb_past_progressive_tense():
  sentences = verb_past_progressive_tense_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_past_progressive_tense"]})
  display(sentences, nlp)


verb_present_perfect_tense_sentences = [
  "It has changed a lot. lt's more beautiful than before.",
  "Because I haven't finished my task yet.",
  "I have checked this mobile phone online.",
  "Never have I met such a person before.",
  "During the last three decades, the number of people participating in physical fitness programs has increased sharply.",
  "Andy, with his parents, has gone to Hong Kong, and they will stay there for a week.",
  "In the last few months, Kenny has been fined more than 1,000 dollars for breaking traffic rules.",
  "We have celebrated the festival since the first pioneers arrived in America.",
  "This medicine has saved millions of people's lives since it was put into use.",
  "Andy doesn't want to see the film Coco because he has seen it twice.",
  "And how have humans altered the environment to get the water we need?",
  "Guatemala has been known by many names, including Cuauhtemalan, a name given to the area by Clash colon warriors accompanying Spanish conquistadors.",
  "So with fertile soil, the political power structure, and the rise of colonialism, and Europeans swooping in to create plantations, bananas have been stamped into Guatemalan history.",
  "A great deal of time, effort, and money has been spent studying hurricanes, so we know some things.",
  "But since the 1980s, one fifth of the Amazon has been deforested as we build more towns, roads, dams, farms, and mines.",
  "The destruction of the Aral Sea has been called the worst environmental disaster of the 20th century.",
  "But as pieces broke off, they could have been compacted into sedimentary rock or changed into metamorphic rock.",
  "In the years following the Revolution, the plate tectonics theory has been fine-tuned.",
  "And the ridges have been cut through and further eroded by rivers.",
  "They've been plowed to produce crops, dug into for sand and gravel, and paved over by concrete and tarmac.",
  "And languages, phrases or even individual words have been borrowed and mangled like we're playing an uncountable number of games of telephone all at once.",
  "And we haven't even gotten into dialects or accents.",
  "His descriptions of how to draw a two-dimensional map of our three-dimensional world have been so celebrated that Western geographers sometimes call him the father of geography.",
  "The people in a diaspora may not have been born in the place they have a cultural affinity for, but at some level, there's a desire to keep a cultural or even physical connection to that place.",
  "Before the industrial revolution, every country would have been considered a stage 1 country, but today none exist.",
  "Since the mid-1920s, Venezuela's economy has been based on oil exports, which we think of as bringing in a lot of wealth.",
  "But sanctions have also been imposed because countries disapprove of the increasingly restrictive socialist government structure, which in this case means the economy is structured so that the state owns and controls large parts of it.",
  "Colonizers have been known to antagonize existing ethnic conflicts or create new ones by promoting one group over another and making sure both groups know why, which ultimately meddles in both local politics and culture.",
  "Historically, Lebanon has been considered a wealthy place, but unlike the UAE, Lebanon has struggled to overcome the politics related to its colonial past and has had political and economic setback after setback.",
  "But so far, we haven't come up with the best term.",
  "For the last few decades, the agrarian crisis has been tied to the complex web of the wider global economic system which international trade plays a crucial role in.",
  "Bt cotton has been modified to produce Bacillus thuringiensis toxin, an insecticide which is supposed to kill a common cotton pest in India called the American bull worm.",
  "But more recently, traditional ways of eating have been systemically broken.",
  "Like we saw last time, foods have been domesticated pretty much everywhere because hunger and access to food is something we've been trying to figure out forever.",
  "Lithium has increasingly been used to make batteries, because it easily conducts a current, it's light, and its structure makes it possible to reset its ions and electrons through recharging, especially when used with cobalt.",
  "All together, transportation, agglomeration and labor have been used to explain the rise of car factories and steel factories from Pittsburgh to Chicago in the 19th and 20th centuries.",
]

def test_verb_present_perfect_tense():
  sentences = verb_present_perfect_tense_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_present_perfect_tense"]})
  display(sentences, nlp)


verb_past_perfect_tense_sentences = [
  "The boy was lying on the ground and he had laid bicycle behind the big tree.",
  "She had put all her effort into her work before she got ill.",
  "By the time I got up, my mother had cooked the breakfast well."
  "He had been in our school for nine years since he came in 2000.",
  "The teacher had been away from the office for a few minutes when we arrived.",
  "When I got to the cinema yesterday, the film had been on for several minutes.",
  "We hadn't seen each other since finishing middle school.",
  "He had learned to play the piano before he was 11 years old.",
  "She didn't pass the exams because she hadn't prepared her lessons well.",
  "His plane had taken off by the time I arrived there.",
  "But through war, slavery and intermarriage, this population had largely been eradicated or assimilated by the time sugar plantations were started on Trinidad by the Spanish in the 1780s and 90s.",
  "But though cholera has been seen all over the world throughout history, until 2010 it hadn't appeared in Haiti for at least 100 years and possibly never at all.",
]
def test_verb_past_perfect_tense():
  sentences = verb_past_perfect_tense_sentences
  #sentences = more
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_past_perfect_tense"]})
  display(sentences, nlp)


verb_copular_sentences = [
  "The poor boy went blind at the age of three.",
  "His voice sounds as if he has a cold.",
  "When I went home yesterday, it was getting dark.",
  "The flowers in the garden smell sweet.",
  "He appears much younger than he really is.",
  "You look very pale. Do you feel sick?",
  "His wish to become a driver has come true.",
  "Her father has become a writer.",
  "Nancy's father looks young and Tony looks like his father.",
  "Some of the apples are bad, but I believe the rest taste sweet.",
]

def test_verb_copular():
  sentences = verb_copular_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_copular"]})
  display(sentences, nlp)


verb_non_finite_sentences = [
  "Understanding your own needs and styles of communication is as important as learning to convey your affection and emotions.",
  "Tasting terrible, the medicine was thrown away by the child.",
  "Tara, remember to lock the door when you leave the office.",
  "Bats are surprisingly long lived creatures, some having a life span of around 20 years.",
  "Most colleges now offer first-year students a course specially designed to help them succeed academically and personally.",
  "Time, used correctly, is money in the bank.",
  "The discovery of new evidence led to the thief being caught.",
  "I looked up and noticed a snake winding its way up the tree to catch its breakfast.",
  "To catch the early flight, we ordered a taxi in advance and got up very early.",
  "Drawing upon his years of experience in the business, Zhang Yong, Alibaba's newly appointed CEO, came up with a novel idea for increasing sales.",
]

verb_modal_sentences = [
  "It wasn't right to me that such near neighbors should not know one another.",
  "We'll make the final decision on our scheme. Should you change your mind, please inform us as soon as possible.",
  "- Can I pay the bill by check? - Sorry, sir. But it is the management rules of our hotel that payment shall be made in cash.",
  "Mark needn't have hurried. After driving at top speed, he arrived half an hour early.",
  "I love the weekend, because I needn't get up early on Saturdays and Sundays.",
  "Lack of sleep can lead to weakened immunity and memory, and also slow physical growth.",
  "- Must you disturb me now? I'm busy preparing a report. - Terribly sorry, but I have something urgent to tell you.",
  "- Mum, little Ray broke his toys again! - It doesn't matter. You see, accidents will happen.",
  "Using AI, many companies are now conducting experiments that couldn't have been possible just a few years ago.",
  "Peter searched all the places where he might have left his iPad but it was all in vain.",
]

def test_verb_modal():
  sentences = verb_modal_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_modal"]})
  display(sentences, nlp)


verb_auxiliary_sentences = [
  "Do you help him with his English every evening?",
  "He is not good at maths.",
  "What other subjects will they have next term?",
  "Has Julian been to Thiland already?",
  "They have not arrived at the hotel yet.",
  "Who is under the tree?",
  "What was he doing last night?",
  "They have lunch erarly, haven't they?",
  "Amy worked hard at school. So she did.",
  "Louise is very good at study. - So am I.",
]

verb_intransitive_sentences = [
  "I think he lives at No.386 West Street.",
  "The key will be left on the table when I leave.",
  "Have you dealt with these letters yet?",
  "We cannot say for sure what will happen.",
  "The cooking time needed depends on the size of the potato.",
]

verb_transitive_sentences = [
  "I always reach school at 7:00 am.",
  "I can't see it clearly.",
  "The Great Wall is the place which almost all tourists would like to visit when they come to Beijing.",
  "The key will be left on the table when I leave.",
  "We'll discuss the problem at the meeting.",
  "With the help of the computer, information can reach every corner of the world swiftly.",
  "There's an invisible force shaping our lives, affecting the weather, climate, land, economy and whether a flag looks majestic or just kind of sits there.",
  "And buried in each layer of ice is evidence of past atmospheric conditions, tiny air bubbles which act like time capsules.",
  "If a bit of biomass is eaten, it passes on its chemical energy to continue the energy flow.",
  "As the liquid water molecules evaporated, they left behind all the salt that had been dissolved in this water.",
  "In the nearby fields, Aral Sea water would still be pumped in for the crops, but rapid evaporation continued to leave behind a thick crust of salt on the soil.",
  "Soils bring together all four spheres of physical geography.",
  "It took many scientists many years to put together all the puzzle pieces to tell the story of how Earth's broken outer shell rises from the mantle and falls back in.",
  "Basically all the places we said, rivers got their water.",
  "Take for instance Indonesia, specifically the island of Java.",
  "Ultimately the people advocating to put back the name Denali had less power and influence and could be ignored.",
  "Artifacts like al-Adrisi's map leave behind clues about how people interacted with and saw the world, just like Ptolemy's.",
  "The people in a diaspora may not have been born in the place they have a cultural affinity for, but at some level, there's a desire to keep a cultural or even physical connection to that place.",
  "Many migrants only migrate internationally when they feel they have no other option, because an international move can mean leaving behind cultural and family networks which provide emotional support.",
  "This particular disease brought with it morbidity, which is another way of saying infected with a disease and had a specific mortality rate or the number of deaths in a given population over a set period of time.",
  "Since the mid-1920s, Venezuela's economy has been based on oil exports, which we think of as bringing in a lot of wealth.",
  "Throw together disagreements over identity and sovereignty with the interests of larger more powerful countries and sprinkle in a dash of lucrative resources and we've got a recipe for conflict.",
  "And radiating out from the central market to the periphery are zones of disamenity, which are corridors of squatter settlements made up of thousands of people in the city who can't afford a house or land, but who still need a place to live.",
  "With nowhere for water to go, it will move really fast through the floodplain and into the next body of water, causing, you guessed it, frequent flashy flooding.",
]

def test_verb_transitive():
  sentences = verb_transitive_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_transitive"]})
  display(sentences, nlp)

_sentences = verb_passive_voice_sentences + verb_simple_present_tense_sentences + verb_simple_past_tense_sentences + verb_simple_future_tense_sentences
_sentences = _sentences + verb_present_progressive_tense_sentences + verb_past_progressive_tense_sentences + verb_present_perfect_tense_sentences
_sentences = _sentences + verb_past_perfect_tense_sentences + verb_copular_sentences + verb_non_finite_sentences + verb_modal_sentences
_sentences = _sentences + verb_auxiliary_sentences + verb_transitive_sentences + verb_intransitive_sentences


def test_verb():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["VERB"]})
  display(sentences, nlp)


