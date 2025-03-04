from kg_detective.en import rules as en_rules
from kg_detective.en.kg_fn import LABEL_RULES as EN_LABEL_RULES
from kg_detective.en.kg_translation import kg_en_cn

from kg_detective.de import rules as de_rules
from kg_detective.de.kg_fn import LABEL_RULES as DE_LABEL_RULES
from kg_detective.de.kg_translation import kg_de_cn

from kg_detective.es import rules as es_rules
from kg_detective.es.kg_fn import LABEL_RULES as ES_LABEL_RULES
from kg_detective.es.kg_translation import kg_es_cn

from kg_detective.kg import get_all_rules

import pkgutil

def print_modules(LABEL_RULES, rules=None, translation={}):
  package = rules
  module_names = []
  for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    module_names.append(modname) 
    #print(modname)
    #print("Found submodule {} (is a package: {})".format(modname, ispkg))

  defined_rule_names = get_all_rules(LABEL_RULES)

  for name in module_names:
    #pass
    assert(name in defined_rule_names)

  for name in defined_rule_names:
    #print(name+".py")
    assert(name in module_names)

  for name in defined_rule_names:
    assert name in translation 
 
def test_modules():
  print_modules(EN_LABEL_RULES, en_rules, kg_en_cn)
  #print_modules(DE_LABEL_RULES, de_rules, kg_de_cn)
  print_modules(ES_LABEL_RULES, es_rules, kg_es_cn)
