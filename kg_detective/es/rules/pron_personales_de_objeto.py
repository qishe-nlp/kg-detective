from spacy.matcher import Matcher, DependencyMatcher
from kg_detective.lib import clean_merge, mark

def search_out(doc, nlp):
  """Search for  

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """
  patterns = [
    [{"POS": "PRON", "DEP": "obj", "MORPH": {"IS_SUPERSET": ["Case=Acc", "PrepCase=Npr", "PronType=Prs"]}}],
  ]

  raw_matches = []

  rule_name = "pron_personales_de_objeto"

  dep_matcher = DependencyMatcher(nlp.vocab)

  verb_iobj_obj = [
    {
      "RIGHT_ID": "verb",
      "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
      "LEFT_ID": "verb",
      "REL_OP": ">--",
      "RIGHT_ID": "iobj",
      "RIGHT_ATTRS": {"POS": "PRON", "MORPH": {"IS_SUPERSET": ["Case=Dat"]}}
    },
    {
      "LEFT_ID": "verb",
      "REL_OP": ">--",
      "RIGHT_ID": "obj",
      "RIGHT_ATTRS": {"POS": "PRON", "DEP": "obj", "MORPH": {"IS_SUPERSET": ["Case=Acc"]}}
    },
  ]

  dep_matcher.add(rule_name, [verb_iobj_obj])

  matches = dep_matcher(doc)
  for index, (_, [verb_id, iobj_id, obj_id]) in enumerate(matches):
    verb_core = doc[verb_id]
    iobj_core = doc[iobj_id]
    obj_core = doc[obj_id]

    raw_matches.append((iobj_id, iobj_id+1, {"sign": "iobj", "iobj_lemma": iobj_core.lemma_, "gid": index})) 
    raw_matches.append((obj_id, obj_id+1, {"sign": "obj", "obj_lemma": obj_core.lemma_, "gid": index})) 
    raw_matches.append((verb_id, verb_id+1, {"sign": "verb", "verb_lemma": verb_core.lemma_, "gid": index})) 

  dep_matcher.remove(rule_name)

  base_index = len(raw_matches)//3

  verb_obj = [
    {
      "RIGHT_ID": "verb",
      "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
      "LEFT_ID": "verb",
      "REL_OP": ">--",
      "RIGHT_ID": "obj",
      "RIGHT_ATTRS": {"POS": "PRON", "DEP": "obj", "MORPH": {"IS_SUPERSET": ["Case=Acc"]}}
    },
  ]

  dep_matcher.add(rule_name, [verb_obj])

  matches = dep_matcher(doc)
  for index, (_, [verb_id, obj_id]) in enumerate(matches):
    verb_core = doc[verb_id]
    obj_core = doc[obj_id]

    raw_matches.append((obj_id, obj_id+1, {"sign": "obj", "obj_lemma": obj_core.lemma_, "gid": base_index+index})) 
    raw_matches.append((verb_id, verb_id+1, {"sign": "verb", "verb_lemma": verb_core.lemma_, "gid": base_index+index})) 

  dep_matcher.remove(rule_name)

  base_index = (len(raw_matches)-base_index*3)//2 + base_index

  verb_iobj = [
    {
      "RIGHT_ID": "verb",
      "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
      "LEFT_ID": "verb",
      "REL_OP": ">--",
      "RIGHT_ID": "iobj",
      "RIGHT_ATTRS": {"POS": "PRON", "MORPH": {"IS_SUPERSET": ["Case=Dat"]}}
    },
  ]

  dep_matcher.add(rule_name, [verb_iobj])

  matches = dep_matcher(doc)
  for index, (_, [verb_id, iobj_id]) in enumerate(matches):
    verb_core = doc[verb_id]
    iobj_core = doc[iobj_id]

    raw_matches.append((iobj_id, iobj_id+1, {"sign": "iobj", "iobj_lemma": iobj_core.lemma_, "gid": base_index+index})) 
    raw_matches.append((verb_id, verb_id+1, {"sign": "verb", "verb_lemma": verb_core.lemma_, "gid": base_index+index})) 

  dep_matcher.remove(rule_name)

  refined_matches = clean_merge(raw_matches)

  return mark(doc, refined_matches)

   
