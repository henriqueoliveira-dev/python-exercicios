"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import heapq


class FilaPrioridades:

    def __init__(self):
        self.fila = []

    def enqueue(self, prioridade, elemento):
        heapq.heappush(self.fila, (prioridade, elemento))

    def dequeue(self):

        if not self.isEmpty():
            return heapq.heappop(self.fila)[1]

        else:
            return "A fila está vazia!"

    def isEmpty(self):
        return len(self.fila) == 0

    def getSize(self):
        return len(self.fila)


# Testando a classe

fila_p = FilaPrioridades()

fila_p.enqueue(3, "Tarefa normal 1")
fila_p.enqueue(1, "Tarefa urgente 1")
fila_p.enqueue(2, "Tarefa importante 1")
fila_p.enqueue(3, "Tarefa normal 2")
fila_p.enqueue(1, "Tarefa urgente 2")
fila_p.enqueue(2, "Tarefa importante 2")


# Retirando os elementos da fila
print(fila_p.dequeue())
print(fila_p.dequeue())
print(fila_p.dequeue())
print(fila_p.dequeue())
print(fila_p.dequeue())
print(fila_p.dequeue())
