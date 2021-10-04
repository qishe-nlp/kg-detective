def search_out(doc, nlp):
  result = [t for t in doc if t.like_num and t.pos_=="ADJ"]
  return result
   
