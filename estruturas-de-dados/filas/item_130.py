"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 17
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#📌 Opção 1 — Inserção e Chamada Manual da Fila

from collections import deque

fila = deque()

fila.append(1)
fila.append(2)
fila.append(3)
fila.append(4)

contador_1 = fila.popleft()
contador_2 = fila.popleft()
contador_3 = fila.popleft()
contador_4 = fila.popleft()

print(f"Senha chamada: N{contador_1:03}")
print(f"Senha chamada: N{contador_2:03}")
print(f"Senha chamada: N{contador_3:03}")
print(f"Senha chamada: N{contador_4:03}")
