import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "en"
pkg = PKG_INDICES[lang]

pron_personal_sentences = [
  "My parents are going to take me to Mount. Wuyi this summer holiday.",
  "I find it difficult to finish the work on time. We only have three hours left.",
  "This morning Diana invited me to her birthday party.",
  "Mike said that the video tapes on the table belonged to him.",
  "Jack and I are good friends.",
  "- Why are you so happy? - That's because an old friend of mine is coming.",
  "Miss Li is our English teacher. She teaches us English very well.",
  "Miss Li teaches us Chinese every day.",
  "I have news for you. It is good news.",
  "Mary needs our help. Let's go and help her.",
]

def test_pron_personal():
  sentences = pron_personal_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_personal"]})
  display(sentences, nlp)


pron_possessive_sentences = [
  "The lovely girl is from Class 6. Her name is Alice.",
  "This is my English book, and yours is on the desk.",
  "My father is a teacher. He loves his students very much.",
  "The iPad isn’t his. It belongs to me.",
  "- Is this your MP3, Kathy? - No. Mine is in the bag.",
  "- Where is my pen? Have you seen it? - Oh, sorry. I have taken yours by mistake.",
  "Bill is not his brother. He is her brother.",  
  "This isn’t her book. Hers is on the desk.",
  "- Is this your ruler? - No, it isn't. It's his.",
  "- Wow, your new bicycle looks the same as mine. - Really?",
]

def test_pron_possessive():
  sentences = pron_possessive_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_possessive"]})
  display(sentences, nlp)


pron_reflexive_sentences = [
  "- Who teaches you English? - No one. I teach myself.",
  "- Help yourself to some cakes, Jim. - Thank you.",
  "- How was your visit to the World Park in Beijing? - Wonderful! We enjoyed ourselves very much.",
  "- How did your uncle learn to play the guitar? - By himself.",
  "- I could look after myself when I was five. - Really? I can't believe it.",
  "Teenagers should learn to protect themselves from all kinds of danger.",
  "- Can you cook by yourself? - Yes, I can cook well.",
  "The film ifself is very fun. ",
  "Don't worry about your daughter, she can look after herself well.",
  "- Look at this model ship. I made it all by myself last week.    - Wow, you are so smart!",
]

def test_pron_reflexive():
  sentences = pron_reflexive_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_reflexive"]})
  display(sentences, nlp)


pron_demostrative_sentences = [
  "- Have you got any books on English grammar? I want to borrow one. - Yes, here you are. But you must return it by Friday.",
  "- I like the story of Murder in a Country House better than that of Unusual Weekend. - I agree. The actors act better than those in Unusual Weekend.",
  "- What is this? - It is a purse.",
  "The weather in summer here is cooler than that in Beijing.",
  "Your home town is really nice! The air quality is as good as one of Sanya.",
  "These are my brother and sister.",
  "This is my uncle and those are my grandparents.",
  "- Simon, this is my cousin Andy. - Nice to meet you, Andy.",
  "Your mobile phone is so good. Where did you buy it? I want to buy one too.",
  "It is really hard for them to climb Mount Huang.",
]

def test_pron_demostrative():
  sentences = pron_demostrative_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_demostrative"]})
  display(sentences, nlp)


pron_indefinite_sentences = [
  "- What do you think of these two books? - Both of them are interesting. And I've read them several times.",
  "- Tom, supper is ready. - I don't want to eat anything, Mum. I'm not feeling well.",
  "My family has two dogs. One is white, the other is black.",
  "- Your tea smells great! - It’s from India. Would you like some?",
  "There has never been such a beautiful village anywhere in the world.",
  "- Which basketball player do you like best, Kobe, James or Jordan? - None of them. Lin Shuhao is my favourite.",
  "- Which would you like, tea or coffee? - Either is OK, I don't mind.",
  "- Look! We have little sugar. - Really? Let's go and buy some.",
  "Today, too many trees are still being cut down somewhere in the world.",
  "All of the boys in Class Four are playing games.",
]

def test_pron_indefinite():
  sentences = pron_indefinite_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_indefinite"]})
  display(sentences, nlp)


pron_relative_sentences = [
  "The policeman has caught the thief who stole Mr.Li's wallet.",
  "Xiandao Lake in Yangxin is the famous place that we'll visit next week.",
  "- Who won the first prize in English speech contest? - The prize went to the girl whose speech was the most natural and fluent.",
  "Shiyan is one of the best places that people would like to visit.",
  "- Is that all? - Yes. That's all what I want to take.",
  "A friend is someone who says, 'What! You too? I thought I was the only one!'",
  "The dog which played with you just now is mine.",
  "You are talented young adults who are full of hope for the future.",
  "This is the book which tells many English stories.",
  "A Wechat is an invention which can help people talk to friends, share photos, ideas and feelings freely.",
]

def test_pron_relative():
  sentences = pron_relative_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_relative"]})
  display(sentences, nlp)


pron_interrogative_sentences = [
  "- Jack, who is your English teacher? - Mrs.Lean.",
  "- Who is that tall woman? - She's my aunt Martha.",
  "- Jenny, whose books are these? - They are Tom's.",
  "- What did your father do last night? - He read a book.",
  "Whatever you do, don’t miss this exhibition, for it’s so hard for me to get the tickets.",
  "There are so many kinds of computers in the shop. I really don't know which to choose.",
  "- Which is your pencil? - The pink one.",
  "- Whose T-shirt is this? - I think it’s Tom’s.",
  "- Who will you ask for help when you get into trouble? - My parents, I think.",
  "- What is your father? Does he still work as an engineer? - Yes, he has been an engineer for thirty years.",
]

def test_pron_interrogative():
  sentences = pron_interrogative_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["pron_interrogative"]})
  display(sentences, nlp)

def test_pron():
  sentences = pron_personal_sentences + pron_possessive_sentences + pron_reflexive_sentences + pron_demostrative_sentences
  sentences = sentences + pron_indefinite_sentences + pron_relative_sentences + pron_interrogative_sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["PRON"]})
  display(sentences, nlp)


