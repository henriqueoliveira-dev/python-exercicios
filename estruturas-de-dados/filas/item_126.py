"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 10
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

from collections import deque

fila = deque()

fila.append("Ana")
fila.append("Bruno")
fila.append("Carlos")
fila.append("Daniel")

nome_1 = fila.popleft()
nome_2 = fila.popleft()
nome_3 = fila.popleft()
nome_4 = fila.popleft()

print(f"Antendo: {nome_1}")
print(f"Antendo: {nome_2}")
print(f"Antendo: {nome_3}")
print(f"Antendo: {nome_4}")
