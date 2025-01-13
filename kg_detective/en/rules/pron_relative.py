from kg_detective.lib import mark

def search_out(doc, nlp):
  """Search for relative pronouns 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Token
  """


  _result = [t for t in doc if t.tag_ in ["WP", "WP$", "WDT", "WRB"] and t.dep_ in ['nsubj', 'dobj', 'poss']]

  refined_matches = [(t.i, t.i+1, {"sign": "relative_pron", "gid": index}) for index, t in enumerate(_result)]

  return mark(doc, refined_matches)
