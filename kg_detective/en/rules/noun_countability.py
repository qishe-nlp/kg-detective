def search_out(doc, nlp):
  """Search for countable and uncountable nouns 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Token
  """

  result = [t for t in doc if t.tag_ in ["NN", "NNS"]]
  return result
