"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 20
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

from collections import deque

fila = deque()

for i in range(1, 6):
    fila.append(i)
    print(f"Numeros da Lista: {i}")

print("------------------------")

for i in range(5):
    numero = fila.popleft()
    print(f"Numero {numero} sendo removido.")

print("------------------------")
