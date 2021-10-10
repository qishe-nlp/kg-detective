from spacy.matcher import DependencyMatcher
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

  dep_matcher = DependencyMatcher(nlp.vocab)
  dep_patterns = [
    [
      {
        "RIGHT_ID": "P",
        "RIGHT_ATTRS": {"POS": "VERB", "DEP": "ROOT"}
      },
      {
        "LEFT_ID": "P",
        "REL_OP": ">",
        "RIGHT_ID": "S",
        "RIGHT_ATTRS": {"DEP": "nsubj"}
      },
    ],
  ]
  dep_matcher.add("simple_s_p", dep_patterns)
  matches = dep_matcher(doc)

  for _, (P, S) in matches:
    subj_span = " ".join([e.text for e in doc[S].subtree])
    result.append(subj_span)
    result.append(doc[P].text)


  return result
   
