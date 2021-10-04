def search_out(doc, nlp):
  """Search for verbs with verb modal   

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed

  Returns:
    list: list of spacy.tokens.Span
  """

  result = []

  result = [t for t in doc if t.tag_=="MD"]
  return result
   
