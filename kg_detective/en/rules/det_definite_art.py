def search_out(doc, nlp):
  ARTS = ["the"]
  result = [t for t in doc if t.text.lower() in ARTS]
  return result
   
