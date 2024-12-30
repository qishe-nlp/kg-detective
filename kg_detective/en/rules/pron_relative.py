def search_out(doc, nlp):
  """Search for relative pronouns 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Token
  """


  _result = [t for t in doc if t.tag_ in ["WP", "WP$", "WDT", "WRB"] and t.dep_ in ['nsubj', 'dobj', 'poss']]

  result = []
  s = 0
  for index, t in enumerate(_result):
    i = t.i
    if i > s:
      result.append({"text": doc[s:i].text}) 
    result.append({"text": t.text, "meta": {"sign": "relative_pron", "gid": index}})
    s = i+1
  if s < len(doc):
    result.append({"text": doc[s:].text})
  return result
