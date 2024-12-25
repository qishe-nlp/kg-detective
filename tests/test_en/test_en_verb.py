import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

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
]

def test_verb_passive_voice():
  sentences = verb_passive_voice_sentences 

  nlp = spacy.load(pkg)
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
  "Linda, why were you late for school yesterday? Because l woke up late.",
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

def test_verb_intransitive():
  sentences = verb_intransitive_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["verb_intransitive"]})
  display(sentences, nlp)

verb_transitive_sentences = [
  "I always reach school at 7:00 am.",
  "I can't see it clearly.",
  "The Great Wall is the place which almost all tourists would like to visit when they come to Beijing.",
  "The key will be left on the table when I leave.",
  "We'll discuss the problem at the meeting.",
  "With the help of the computer, information can reach every corner of the world swiftly.",
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


