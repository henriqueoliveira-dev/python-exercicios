"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 13
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

from collections import deque

fila = deque()

for i in range(10):
    numero = (i + 1) * 5
    fila.append(numero)

    numero = fila.popleft()

    print(f"Removendo número: {numero}")

print(f"Elementos da fila: {fila}")
