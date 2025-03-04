from spacy.matcher import Matcher, DependencyMatcher
from kg_detective.lib import clean_merge, mark

def search_out(doc, nlp):
  """Search for  

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """

  patterns = [
    [{"POS": {"IN": ["VERB", "AUX"]}, "MORPH": {"IS_SUPERSET": ["Tense=Past", "VerbForm=Part"]}}],
    [{"POS": "ADJ", "MORPH": {"IS_SUPERSET": ["VerbForm=Part"]}}],
  ]

  raw_matches = []

  rule_name = "verb_participio"

  return []
   
