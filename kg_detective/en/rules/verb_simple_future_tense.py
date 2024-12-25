from spacy.matcher import DependencyMatcher
from kg_detective.lib import merge

def search_out(doc, nlp):
  """Search for verbs with simple future tense 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """

  result = []

  dep_matcher = DependencyMatcher(nlp.vocab)

  will_verb = [
    {
      "RIGHT_ID": "core_verb",
      "RIGHT_ATTRS": {"POS": {"IN": ["VERB", "AUX"]}, "TAG": {"IN": ["VB", "VBN"]}}
    },
    {
      "LEFT_ID": "core_verb",
      "REL_OP": ">",
      "RIGHT_ID": "aux",
      "RIGHT_ATTRS": {"DEP": "aux", "POS": "AUX", "lemma": "will"}
    },
  ]
  be_verb_ing = [
    {
      "RIGHT_ID": "core_verb",
      "RIGHT_ATTRS": {"POS": "VERB", "TAG": "VBG"}
    },
    {
      "LEFT_ID": "core_verb",
      "REL_OP": ">",
      "RIGHT_ID": "aux",
      "RIGHT_ATTRS": {"DEP": "aux", "POS": "AUX", "lemma": "be"}
    }
  ]

  dep_patterns = [will_verb, be_verb_ing]
  dep_matcher.add("verb_simple_future_tense", dep_patterns)
  matches = dep_matcher(doc)
  dep_ranges = [(token_ids[-1], token_ids[0]+1) for _, token_ids in matches]

  # merge ranges
  refined_matches = merge(dep_ranges)
  s = 0
  for start, end in refined_matches:
    if start > s:
      span = doc[s:start].text
      result.append({"text": span, "highlight": False})
    span = doc[start:end].text
    result.append({"text": span, "highlight": True})
    s = end
  if s < len(doc):
    span = doc[s:].text
    result.append({"text": span, "highlight": False})
 
  return result
