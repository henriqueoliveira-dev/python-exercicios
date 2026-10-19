"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 8
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#📌 Exercício 5 — Fila de Atendimento

from collections import deque

fila = deque()

fila.append("Cliente 1")
fila.append("Cliente 2")
fila.append("Cliente 3")



cliente_1 = fila.popleft()
cliente_2 = fila.popleft()

print(f"Clientes atendidos: {cliente_1}, {cliente_2}")

print(f"Clientes restantes: {fila}")
