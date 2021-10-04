def search_out(doc, nlp):
  """Search for adjective with -ing as its ending

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Token
  """
  result = [t for t in doc if t.pos_=="ADJ" and t.tag_=="JJ" and len(t.text)>4 and t.text[-3:]=="ing"]
  return result
   
