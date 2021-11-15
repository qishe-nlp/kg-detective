from spacy.matcher import Matcher, PhraseMatcher, DependencyMatcher
from kg_detective.lib import merge

def search_out(doc, nlp):
  """Search for  

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """
  result = []

  token_matcher = Matcher(nlp.vocab)
  patterns = [
    [{"POS": "PRON", "DEP": "obj", "MORPH": {"IS_SUPERSET": ["Case=Acc", "PrepCase=Npr", "PronType=Prs", "Reflex=Yes"]}, "OP": "?"}, {"POS": "AUX", "LEMMA": "haber", "MORPH": {"IS_SUPERSET": ["Mood=Ind", "Tense=Fut", "VerbForm=Fin"]}}, {"POS": "VERB", "MORPH": {"IS_SUPERSET": ["Tense=Past", "VerbForm=Part"]}}],
  ]
  token_matcher.add("verb_indicativo_futuro_perfecto", patterns)

  matches = token_matcher(doc)
  token_ranges = [(start, end) for _, start, end in matches]

  refined_matches = merge(token_ranges)
  for start, end in refined_matches:
    span = doc[start:end].text
    result.append({"text": span})


  return result
   
