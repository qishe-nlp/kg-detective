from tests.lib import *


def write_sens(lang):
  data = get_lang_sens(lang)
  for name, sens in data.items():
    filename = "{}_sens/{}.json".format(lang, name)
    write_to_json(filename, sens)

def test_gen_en_sens():
  lang = "en"
  write_sens(lang)


def test_gen_de_sens():
  lang = "de"
  write_sens(lang)

def test_gen_es_sens():
  lang = "es"
  write_sens(lang)
