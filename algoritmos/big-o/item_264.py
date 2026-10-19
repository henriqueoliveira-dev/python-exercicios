"""Conteúdo extraído de: 12_Big-O.ipynb_1_VaRqNN.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def lista1():
  lista = []
  for i in range(1000):
    lista += [i]
  return lista

print(lista1())
len(lista1())
