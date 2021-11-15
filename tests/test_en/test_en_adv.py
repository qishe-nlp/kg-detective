import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

adv_of_frequency_sentences = [
  "Our teacher is often late.",
  "My father hardly ever watches football on TV.",
  "He doesn't usually go to bed late.",
  "I will visit England sometime next summer.",
  "Tom never listens to the radio.",
  "Is your teacher always in class on time?",
  "He doesn't always go to class.",
  "What time do you usually get up at the weekend?",
  "Mark is always busy.",
  "I often go to KFC.",
]

def test_adv_of_frequency():
  sentences = adv_of_frequency_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_of_frequency"]})
  display(sentences, nlp)

adv_of_manner_sentences = [
  "Please, drive your car carefully tomorrow.",
  "Our team are playing badly and will probably lose.",
  "We were playing quietly in our room all night.",
  "Usually they were quickly sent to their rooms if they misbehaved.",
  "Thousands of people are wrongly imprisoned in the US every year.",
]

def test_adv_of_manner():
  sentences = adv_of_manner_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_of_manner"]})
  display(sentences, nlp)

adv_of_time_sentences = [
  "She liked the present very much last night.",
  "They were dancing quietly in our room all night.",
  "David walks to work every morning.",
  "Dick went there late yesterday.",
  "With the computer down, we could no longer continue our work.",
  "Liu Yun visited her uncle yesterday.",
  "They're going to have a farewell party this evening.",
  "I eat a sandwich every day.",
]

def test_adv_of_time():
  sentences = adv_of_time_sentences 
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_of_time"]})
  display(sentences, nlp)


adv_of_place_sentences = [
  "He is playing quietly in his room all day.",
  "The man was wrongly imprisoned in the US last night.",
  "Li Xiao almost died in his home yesterday.",
  "Did you learn a lot at school today?",
  "My brother would like to go somewhere noisy.",
  "She often gets home very late."
  "I looked for my pet dog everywhere, but I can't find it anywhere.",
  "Did you arrive there?",
  "They are making too much noise here. Let's go somewhere quiet.",
]

def test_adv_of_place():
  sentences = adv_of_place_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_of_place"]})
  display(sentences, nlp)


adv_of_degree_sentences = [
  "Emma Larson almost died in prison last year.",
  "I could barely see you in the dark.",
  "The work is too difficult for the girl.",
  "This movie wasn't interesting enough.",
  "Some of the students can do very well in English exams, but can hardly understand what a native speaker says.",
  "I think it's impossible for us to work out the plan in just two days. It's too difficult.",
  "You're right. We can't be too careful while working on it.",
  "After practicing for several months, I can swim much faster now.",
  "You seem terribly ill.",
  "We're sure Wenzhou will be even better tomorrow.",
  "I could hardly work it out.",
]

def test_adv_of_degree():
  sentences = adv_of_degree_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_of_degree"]})
  display(sentences, nlp)


adv_for_equal_comparisons_sentences = [
  "Write as carefully as you can and try not to make any mistakes.",
  "Roy thinks he works as hard as his friend, Dan.",
  "Lucy walks as slowly as Lily does.",
  "I like this dress better, but it costs almost twice as much as that one.",
  "Mr. Wang told us to read as carefully as we could.",
  "We know a train in the past can't go as fast as a train at the moment.",
  "He doesn't play the violin as well as his father.",
  "Peter speaks Spanish well indeed, but of course not as fluently as a local speaker in Spain.",
  "He speaks English as fluently as he does Chinese.",
  "Read it as carefully as possible.",
]

def test_adv_for_equal_comparisons():
  sentences = adv_for_equal_comparisons_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_for_equal_comparisons"]})
  display(sentences, nlp)

adv_comparative_sentences = [
  "They arrived earlier than us.",
  "Please, can you drive more slowly?",
  "We work more happily now with the new manager.",
  "She eats better than me.",
  "We finished more quickly than we expected.",
  "Men lose weight more easily than women.",
  "Could you speak more slowly, please?",
  "He threw the javelin farther than all the others.",
]

def test_adv_comparative():
  sentences = adv_comparative_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_comparative"]})
  display(sentences, nlp)

adv_superlative_sentences = [
  "I heard that he speaks English best in the family, but he speaks Chinese worst in the family.",
  "Of all the vegetables, I like the tomato best.",
  "Who can sing the most beautifully in our class?",
  "Who listens the most carefully, Tom, Jack or Bill?",
  "His mother was angry, because he did the worst job in examination in his class.",
  "Who does homework the most carefully in your class?",
  "She goes to the dentist most regularly in her family.",
  "Of all the teams in NBA, I think the Los Angeles Lakes played most successfully this year.",
  "Do you know who can write the most beautifully in your class?",
  "Of all the girls, Lisa danced best. She won the first prize.",
]

def test_adv_superlative():
  sentences = adv_superlative_sentences
 
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_superlative"]})
  display(sentences, nlp)

_sentences = adv_of_frequency_sentences + adv_of_manner_sentences + adv_of_time_sentences + adv_of_place_sentences + adv_of_degree_sentences
_sentences = _sentences + adv_for_equal_comparisons_sentences + adv_comparative_sentences + adv_superlative_sentences

def test_adv():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADV"]})
  display(sentences, nlp)

