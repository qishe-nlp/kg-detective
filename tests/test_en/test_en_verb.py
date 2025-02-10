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
]

def test_verb_simple_past_tense():
  sentences = verb_simple_past_tense_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_simple_past_tense"]})
  display(sentences, nlp)


verb_simple_future_tense_sentences = [
  "I wonder when they will leave for Beijing. I will go to the train station to see them off when they leave.",
  "I will cook Chinese dishes for Louise tomorrow evening.",
  "I will stay at home.",
  "Peter, what will you do next Sunday? We will visit our grandparents.",
  "I will buy some in the supermarket.",
  "He has ordered a watch online for his father and it will be sent to him before Father's Day.",
  "If it isn't fine this weekend, our spring field trip will be cancelled.",
  "There will be a talent show in ten minutes.",
  "The summer vacation will begin next week. David is coming to stay with us.",
  "Tomorrow my dad will cook a big dinner for my birthday party.",
]

def test_verb_simple_future_tense():
  sentences = verb_simple_future_tense_sentences
 
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
  "I am making the paper-cutting with it.",
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
]

def test_verb_past_perfect_tense():
  sentences = verb_past_perfect_tense_sentences
 
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

]

def test_verb_transitive():
  sentences = verb_transitive_sentences
  #sentences = more
 
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


