import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "de"
pkg = PKG_INDICES[lang]

frag_frag_sentences = [
  "- Hallo ich bin Anna, und wer bist du? - Ich bin Lisa.",
  "- Ich wohne in dem Haus da drüben, und wo wohnst du? - Ich wohne in dem Haus neben dir.",
  "- Super. Ich gehe jetzt spielen, was machst du? - Ich gehe jetzt nach Hause, lernen.",
  "- Wann musst du nach Hause gehen? - Um 18 Uhr.",
  "- Kommst du mal zu mir? Ich habe eine tolle Katze. - Ja, sehr gern. Wie heißt deine Katze? - Mimi Kühlschrank!",
  "- Wie bitte? Warum heißt deine Katze 'Mimi Kühlschrank'? - Weil sie immer vor dem Kühlschrank sitzt.",
  "- Woher kommst du? - Ich komme aus China.",
  "- Wie alt bist du? - Ich bin 20.",
  "- Wohin gehst du? - Ich gehe in die Schule.",
  "- Wie geht es Ihnen? - Sehr gut.",
]

def test_frag_frag():
  sentences = frag_frag_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["frag_frag"]})
  display(sentences, nlp)


_sentences = frag_frag_sentences 

def test_frag():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["FRAG"]})
  display(sentences, nlp)


