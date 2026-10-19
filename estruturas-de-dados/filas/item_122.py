"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 2
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#🟡 Jeito 2 — Inserção pelo usuário

#O usuário fornece os valores usando input():

from collections import deque

fila = deque()

for i in range(4):
    numero = int(input("Digite um número: "))
    fila.append(numero)

print(fila)
