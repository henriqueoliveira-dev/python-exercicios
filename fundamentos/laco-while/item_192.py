"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 27
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

lsita = [1,2,3]
interador = iter(lista)

while(True):
  try:
    print(next(interador))
  except StopIteration:
    break
#
