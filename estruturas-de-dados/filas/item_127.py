"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 12
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

from collections import deque

fila = deque()

fila.append(5)
fila.append(10)
fila.append(15)
fila.append(20)
fila.append(25)

nome_1 = fila.popleft()
nome_2 = fila.popleft()
nome_3 = fila.popleft()
nome_4 = fila.popleft()
nome_5 = fila.popleft()

print(f"Removendo numero: {nome_1}")
print(f"Removendo numero: {nome_2}")
print(f"Removendo numero: {nome_3}")
print(f"Removendo numero: {nome_4}")
print(f"Removendo numero: {nome_5}")

print(f"Elementos da lista: {fila}")
