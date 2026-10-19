"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 26
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

lista = [1,2,3,4]
interador = iter(lista)

try:
  print(next(interador))
  print(next(interador))
  print(next(interador))
  print(next(interador))
  print(next(interador)) # Este causará o StopIteration
except StopIteration:
  print("O interador chegou ao fim!")
