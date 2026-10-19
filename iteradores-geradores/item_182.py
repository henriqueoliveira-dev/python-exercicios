"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def anos():
  yield '2000'
  yield '2001'
  yield '2002'
  yield '2003'
  yield '2004'
  yield '2005'

for indice, valor in enumerate(anos()):
  print(indice, valor)
