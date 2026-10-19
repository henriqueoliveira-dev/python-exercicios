"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 26
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

def conta_vogais(texto):
  vogais = 0
  arr_vogais = ("a","e","i","o","u")
  for i in texto:
    if i in arr_vogais:
      vogais += 1
  return vogais

conta_vogais("Olá Mundo")
