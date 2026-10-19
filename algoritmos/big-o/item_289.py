"""Conteúdo extraído de: 13_C_pia_de_Nota_o_Big-O.ipynb_1-Btboet.ipynb
Célula original: 11
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

# O(1000) -> O(n)
def lista1():
  lista = []
  for i in range(1000):
    lista += [i]
  return lista
