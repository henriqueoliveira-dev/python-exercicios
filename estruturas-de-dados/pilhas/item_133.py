"""Conteúdo extraído de: 📚 Exercícios — PILHAS.ipynb
Célula original: 1
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#📌 Exercício 1 — Consultando o Topo da Pilha

pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)

numero = pilha[-1]

print(f"Elemento no topo: {numero}")

pilha.pop()
pilha.pop()
pilha.pop()

print(f"Pilha: {pilha}")
