"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

#Exemplo usando FIFO:

from collections import deque

fila = deque()

fila.append('pessoa 1')
fila.append('pessoa 2')
fila.append('pessoa 3')

primeira_pessoa = fila.popleft() #remove e retorna o elmento do inicio da fila

print(primeira_pessoa)

print(fila)
