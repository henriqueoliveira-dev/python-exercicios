"""Conteúdo extraído de: 📚 Exercícios — FILAS .ipynb
Célula original: 15
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

from collections import deque

fila = deque()

# Verificar se a fila está vazia
if not fila:
    print("Fila está vazia")
else:
    print("Fila não está vazia")


# Adicionar um elemento
fila.append(10)


# Verificar novamente
if not fila:
    print("Fila está vazia")
else:
    print("Fila não está vazia")
