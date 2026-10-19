"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 18
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#📌 Opção 2 — Inserção e Chamada com for

from collections import deque

fila = deque()

# Colocar as 4 senhas na fila
for i in range(1, 5):
    fila.append(i)

# Chamar as 4 senhas
for i in range(4):
    numero = fila.popleft()
    print(f"Senha chamada: N{numero:03}")
