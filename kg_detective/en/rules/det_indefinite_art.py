def search_out(doc, nlp):
  IN_ARTS = ["a", "an"]
  result = [t for t in doc if t.text.lower() in IN_ARTS]
  return result
   
