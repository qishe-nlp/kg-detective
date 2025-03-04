import spacy
from kg_detective import PKG_INDICES
from tests.lib import *

lang = "es"
pkg = PKG_INDICES[lang]

old = [
  "No hables tan alto, por favor.",
  "Habla más bajo.",
  "Vas muy rápido.",
  "No vayas tan rápido.",
  "Ve más lento.",
  "No trabajen tanto.",
  "Trabajen menos.",
  "No gritéis tanto.",
  "Hablo español bien, pero Li habla mejor que yo.",
  "Jorge estudiaba mucho y ahora estudia tanto como antes.",
  "Duermo mucho, pero María duerme más que yo.",
  "Alberto habla mucho y su mujer habla tanto como él.",
  "Enrique bebe poco, pero Manuel bebe aún menos que él.",
]

adv_comparativo_sentences = [
  "No hables tan alto, por favor.",
  "Habla más bajo.",
  "Ve más lento.",
  "Trabajen menos.",
  "Hablo español bien, pero Li habla mejor que yo.",
  "Duermo mucho, pero María duerme más que yo.",
  "Enrique bebe poco, pero Manuel bebe aún menos que él.",
  "Ella corre más rápido que yo.",
  "Habla más claramente que tú.",
  "Él trabaja menos eficientemente que ella.", 
  "Camina menos rápido que su hermano.",
]
def test_adv_comparativo():
  sentences = adv_comparativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_comparativo"]})
  display(sentences, nlp)


adv_igualdad_comparativo_sentences = [
  "No hables tan alto, por favor.",
  "Jorge estudiaba mucho y ahora estudia tanto como antes.",
  "Alberto habla mucho y su mujer habla tanto como él.",
  "Ella corre tan rápido como tú.",
  "Trabaja tan diligentemente como su colega.",
  "Esta falda te queda igual de bien que la otra.",
  "Lo hiciste igual de bien que él.",
  "El SIS de nueva generación logrará funcionar igual de rápido que el de la antigua.",
  "Los padres, por un lado, comen igual de mal que sus hijos.",
]

def test_adv_igualdad_comparativo():
  sentences = adv_igualdad_comparativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_igualdad_comparativo"]})
  display(sentences, nlp)


adv_superlativo_sentences =[
  "Ella es la que corre más rápido de todas.",
  "Él es el que trabaja menos eficientemente del equipo.",
  "De todos ellos, él corrió más rápido.",
  "Este método es el que mejor funciona.",
]

def test_adv_superlativo():
  sentences = adv_superlativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_superlativo"]})
  display(sentences, nlp)

adv_absoluto_superlativo_sentences = [
  "Clara corre rapidísimamente.",
  "Había oído que allá se hacía perfectísimo.",
  "Una de las cosas le impactó muchísimo.",
  "Durante una época me preocupó muchísimo el silencio de los acallados.",
]

def test_adv_absoluto_superlativo():
  sentences = adv_absoluto_superlativo_sentences 

  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"rules": ["adv_absoluto_superlativo"]})
  display(sentences, nlp)

_sentences = adv_comparativo_sentences + adv_igualdad_comparativo_sentences + adv_superlativo_sentences

def test_adv():
  sentences = _sentences
  nlp = spacy.load(pkg)
  nlp.add_pipe('kg', config={"labels": ["ADV"]})
  display(sentences, nlp)


