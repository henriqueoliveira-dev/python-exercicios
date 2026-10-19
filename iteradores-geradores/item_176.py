"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def ancora ():
  yield 1
  yield 2
  yield 3

for item in ancora():
  print(item)
