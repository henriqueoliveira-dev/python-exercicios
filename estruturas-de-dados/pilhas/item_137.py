"""Conteúdo extraído de: 📚 Exercícios — PILHAS.ipynb
Célula original: 9
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

pilha = []

for i in range(1, 6):
    numero = i * 10
    pilha.append(numero)

removidos = []

for i in range(2):
    numero = pilha.pop()
    removidos.append(numero)

print(f"Elementos removidos: {removidos}")
print(f"Pilha depois da remoção: {pilha}")
