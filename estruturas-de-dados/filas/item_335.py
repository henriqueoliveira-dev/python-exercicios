"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

from collections import deque

class DequeDemo:
    def __init__(self):
        self.deque = deque()

    def addFront(self, item):
        self.deque.appendleft(item)

    def addRear(self, item):
        self.deque.append(item)

    def add_to_front(self, item):
        self.deque.appendleft(item)

    def add_to_rear(self, item):
        self.deque.append(item)
