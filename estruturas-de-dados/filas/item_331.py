"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

# Vamos criar uma implementação simples de fila
# em Python usando collections.deque.

from collections import deque

class Fila:

    def __init__(self):

        self.fila = deque()

    # Método para adicionar um elemento à fila. Em termos técnicos de fila,
    # isso é comumente chamado de 'enqueue' (enfileirar).
    def enqueue(self, elemento):

        self.fila.append(elemento)

    def dequeue(self):

        if not self.isEmpty():

            return self.fila.popleft()

        else:
            return "A fila está vazia"

    def isEmpty(self):

        return len(self.fila) == 0

    def front(self):

        if not self.isEmpty():

            return self.fila[0]

        else:
            return "A fila está vazia"

    def rear(self):

        if not self.isEmpty():

            return self.fila[-1]

        else:
            return "A fila está vazia"

    def getSize(self):

        return len(self.fila)

fila = Fila()

print(fila.isEmpty())

fila.enqueue("elemento 1")
fila.enqueue("elemento 2")
fila.enqueue("elemento 3")



print(fila.front())
print(fila.rear())
print(fila.getSize())
print(fila.dequeue())
print(fila.isEmpty())
