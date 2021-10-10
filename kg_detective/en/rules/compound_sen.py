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
        "RIGHT_ID": "A",
        "RIGHT_ATTRS": {"POS": {"IN": ["VERB", "AUX"]}, "DEP": "ROOT"}
      },
      {
        "LEFT_ID": "A",
        "REL_OP": ">",
        "RIGHT_ID": "conj",
        "RIGHT_ATTRS": {"DEP": "cc"}
      },
      {
        "LEFT_ID": "A",
        "REL_OP": ">",
        "RIGHT_ID": "B",
        "RIGHT_ATTRS": {"DEP": "conj"}
      },
    ],
  ]
  dep_matcher.add("compound", dep_patterns)
  matches = dep_matcher(doc)

  for _, (A, conj, B) in matches:
    A_subtrees = [t.subtree for t in doc[A].children if t.dep_ not in ["cc", "conj"]]
    A_span = " ".join(([" ".join([e.text for e in st]) for st in A_subtrees]))
    B_span = " ".join([e.text for e in doc[B].subtree])
    conj_span = doc[conj].text
    result.append(A_span)
    result.append(conj_span)
    result.append(B_span)

  return result
   
