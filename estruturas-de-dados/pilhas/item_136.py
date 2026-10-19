"""Conteúdo extraído de: 📚 Exercícios — PILHAS.ipynb
Célula original: 8
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

#Exercício 4 — Duas Remoções da Pilha com pop()

pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)
pilha.append(50)

numero_1 = pilha.pop()
numero_2 = pilha.pop()

print(f"Elementos removidos: {numero_1}, {numero_2}.")
print(f"Pilha depois da remoção: {pilha}")
