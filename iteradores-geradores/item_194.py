"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 32
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

def duplicado(lista):
  for i in lista:
    yield i*2

lista = [1,2,3,4,5]
for i in duplicado(lista):
  print(i)
