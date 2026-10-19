"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 18
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def gen1():
  yield [1,2]
  yield [3,4]
  yield [4,6]
  yield [5,7]

for x, y in gen1():
  print(x, y)
