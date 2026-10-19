"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 53
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#segunda possibilidade
lista = [1,2,3,4,5,6,7,8,9,10]

pares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Números pares: {pares}")
print(f"Quantidade de números pares: {len(pares)}")
