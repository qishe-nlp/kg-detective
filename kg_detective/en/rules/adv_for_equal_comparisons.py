from spacy.matcher import DependencyMatcher
from kg_detective.lib import merge

def search_out(doc, nlp):
  """Search for adverbs for equal comparisons 

  Args:
    doc (spacy.tokens.Doc): doc to be analyzed
    nlp (spacy.language.Language): context language

  Returns:
    list: list of spacy.tokens.Span
  """
  result = []

  dep_matcher = DependencyMatcher(nlp.vocab)

  # pattern: as adv as pobj
  as_adv_as_pobj = [
    {
      "RIGHT_ID": "A",
      "RIGHT_ATTRS": {"POS": "ADV", "TAG": "RB"}
    },
    {
      "LEFT_ID": "A",
      "REL_OP": ">",
      "RIGHT_ID": "left_as",
      "RIGHT_ATTRS": {"DEP": "advmod", "LOWER": {"IN": ["as", "so"]}}
    },
    {
      "LEFT_ID": "A",
      "REL_OP": ">+",
      "RIGHT_ID": "right_as",
      "RIGHT_ATTRS": {"POS": "ADP", "LOWER": "as"}
    },
    {
      "LEFT_ID": "right_as",
      "REL_OP": ">",
      "RIGHT_ID": "B",
      "RIGHT_ATTRS": {"DEP": "pobj"}
    },
  ]

  dep_matcher.add("adv_equal_comprison", [as_adv_as_pobj])
  matches = dep_matcher(doc)

  raw_matches = []
  for index, (_, [adv_core_id, left_as_id, right_as_id, obj_core_id]) in enumerate(matches):
    adv_core = doc[adv_core_id]
    obj_core = doc[obj_core_id]

    adv_subtree = [list(e.subtree) for e in adv_core.children if e.dep_ not in ["cc", "conj", "punct"]]
    adv_tree = [e.i for e in sum(adv_subtree, [])]
    adv_tree.append(adv_core_id)
    adv_tree.sort()
    obj_tree = [e.i for e in obj_core.subtree]
    obj_tree.sort()

    adv_assertion = len(adv_tree) == adv_tree[-1]-adv_tree[0]+1
    obj_assertion = len(obj_tree) == obj_tree[-1]-obj_tree[0]+1 and obj_tree[0]==right_as_id+1

    if adv_assertion and obj_assertion:    
      raw_matches.append((adv_tree[0], obj_tree[0], {"sign": "as_adv_as", "adv_lemma": adv_core.lemma_, "gid": index}))
      raw_matches.append((obj_tree[0], obj_tree[-1]+1, {"sign": "as_obj", "gid": index}))

  dep_matcher.remove("adv_equal_comprison")

  base_index = len(raw_matches)

  # pattern: as adv as advcl
  as_adv_as_advcl = [
    {
      "RIGHT_ID": "A",
      "RIGHT_ATTRS": {"POS": "ADV", "TAG": "RB"}
    },
    {
      "LEFT_ID": "A",
      "REL_OP": ">",
      "RIGHT_ID": "left_as",
      "RIGHT_ATTRS": {"DEP": "advmod", "LOWER": {"IN": ["as", "so"]}}
    },
    {
      "LEFT_ID": "A",
      "REL_OP": ">",
      "RIGHT_ID": "advcl",
      "RIGHT_ATTRS": {"POS": {"IN": ["VERB", "AUX"]}, "DEP": "advcl"}
    },
    {
      "LEFT_ID": "advcl",
      "REL_OP": ">",
      "RIGHT_ID": "right_as",
      "RIGHT_ATTRS": {"DEP": "mark", "POS": "SCONJ"}
    },
  ]

  # TODO:
  dep_matcher.add("adv_equal_comprison", [as_adv_as_advcl])
  matches = dep_matcher(doc)

  for index, (_, [adv_core_id, left_as_id, advcl_id, right_as_id]) in enumerate(matches):
    adv_core = doc[adv_core_id]
    obj_core = doc[advcl_id]

    adv_subtree = [list(e.subtree) for e in adv_core.children if e.dep_ not in ["cc", "conj", "punct"]]
    adv_tree = [e.i for e in sum(adv_subtree, [])]
    adv_tree.append(adv_core_id)
    adv_tree.sort()
    obj_tree = [e.i for e in obj_core.subtree]
    obj_tree.sort()

    adv_assertion = len(adv_tree) == adv_tree[-1]-adv_tree[0]+1
    obj_assertion = len(obj_tree) == obj_tree[-1]-obj_tree[0]+1 and obj_tree[0]==right_as_id

    if adv_assertion and obj_assertion:    
      raw_matches.append((adv_tree[0], obj_tree[0]+1, {"sign": "as_adv_as", "adv_lemma": adv_core.lemma_, "gid": base_index+index}))
      raw_matches.append((obj_tree[0]+1, obj_tree[-1]+1, {"sign": "as_obj", "gid": base_index+index}))

  dep_matcher.remove("adv_equal_comprison")

  refined_matches = merge(raw_matches)

  # TODO: mark(doc, refined_matches)
  s = 0
  for start, end, meta in refined_matches:
    if start > s:
      text = doc[s:start].text
      result.append({"text": text})
    text = doc[start:end].text
    result.append({"text": text, "meta": meta})
    s = end
  if s < len(doc):
    text = doc[s:].text
    result.append({"text": text})

  return result

