"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 64
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

lista = [
    40,
    30,
    20,
    50,
    98
]
#priemiro elemento da lista
for numero in lista:
    if numero == lista[0]:
      print(f"Primeriro elemento: {numero}")
    #segundo elemento da lista
    elif numero == lista[-1]:
      print(f"Ultimo elemento da lista: {numero}")
#quantidade de elemento da lista
quantidade = len(lista)
print(f"Quantidades de elementos: {quantidade}")
