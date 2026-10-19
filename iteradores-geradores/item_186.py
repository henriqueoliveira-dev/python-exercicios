"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 19
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def gen1():
  yield 1
  yield 2
  yield 3

def gen2():
  for i in gen1():
    yield i, 'a'
    yield i, 'b'
    yield i, 'c'

for x,y in gen2():
  print(x,y)
