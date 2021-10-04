import sys

LABELS = ["NOUN", "ADJ", "ADV", "PREP", "VERB", "PRON", "DETERMINER", "CONJ", "INTERJ"]

NOUN_RULES = ["noun_proper", "noun_countability", "noun_with_indefinite_art", "noun_with_definite_art", "noun_possessive"]

ADJ_RULES = ["adj_ending_in_ed", "adj_ending_in_ing", "adj_order", "adj_for_equal_comparisons", "adj_comparative", "adj_superlative"]

ADV_RULES = ["adv_of_frequency", "adv_of_manner", "adv_of_time", "adv_of_place", "adv_of_degree", "adv_for_equal_comparisons", "adv_comparative", "adv_superlative"]

PREP_RULES = ["prep_of_time", "prep_of_movement", "prep_of_manner", "prep_with_verb", "prep_with_adj", "prep_with_noun"]

VERB_RULES = ["verb_passive_voice", "verb_simple_present_tense", "verb_simple_past_tense", "verb_simple_future_tense", "verb_present_progressive_tense", "verb_past_progressive_tense", "verb_present_perfect_tense", "verb_past_perfect_tense", "verb_copulas", "verb_non_finite", "verb_modal", "verb_auxiliary", "verb_transitive", "verb_intransitive"]

PRON_RULES = ["pron_personal", "pron_possessive", "pron_reflexive", "pron_demostrative", "pron_indefinite", "pron_relative", "pron_interrogative"]

DETERMINER_RULES = ["det_cardinal_num", "det_ordinal_num", "det_indefinite_art", "det_definite_art"]

CONJ_RULES = ["conj_subordinating", "conj_coordinating"]

INTERJ_RULES = ["interj_interj"]

LABEL_RULES = {label: getattr(sys.modules[__name__], label+"_RULES") for label in LABELS}


