def search_out(doc, nlp):
  result = [t for t in doc if t.pos_=="SCONJ"]
  return result
   
