"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 50
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

lista = [122, 198, 1783, 127, 10]

num_maior = lista[0]
num_menor = lista[0]

for numero in lista:
    if numero > num_maior:
        num_maior = numero

    if numero < num_menor:
        num_menor = numero

print(f"Maior: {num_maior}")
print(f"Menor: {num_menor}")
