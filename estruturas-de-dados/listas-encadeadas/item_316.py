"""Conteúdo extraído de: 14_Lista_Encadiadas.ipynb_12rm6IrX.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:

    def __init__(self):
        self.primeiro = None

    def insere_inicio(self, valor):
        novo = No(valor)

        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro

        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def pesquisa(self, valor):
        if self.primeiro == None:
          print("A lista está vazia")
          return None

        atual = self.primeiro
        while atual != None:
            if atual.valor == valor:
                return atual
            atual = atual.proximo

        print("Valor não encontrado")
        return None

    def excluir_inicio(self):
        if self.primeiro == None:
           print("Lista vazia")
           return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


# Criando a lista
lista = ListaEncadeada()

# Inserindo no início
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)

# Mostrando a lista
lista.mostrar()

lista.primeiro
print()

lista.primeiro.mostra_no()
lista.primeiro.proximo.mostra_no()
lista.primeiro.proximo.proximo.mostra_no()
