"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 6
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#📌 Exercício 4 — Duas Remoções da Fila

from collections import deque

fila = deque()

fila.append(10)
fila.append(20)
fila.append(30)
fila.append(40)

numero = fila.popleft()

print(f"Numero removido: {numero}")
print(fila)
