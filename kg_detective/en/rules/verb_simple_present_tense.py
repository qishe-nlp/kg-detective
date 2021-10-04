def search_out(doc, nlp):
  """Search for verbs with simple present tense  

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """

  result = []

  result = [t for t in doc if t.tag_ in ["VBZ", "VBP", "VB"] and not any([c.dep_=="aux" for c in t.children])]
  return result
   
