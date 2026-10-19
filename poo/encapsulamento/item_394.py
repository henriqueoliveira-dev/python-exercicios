"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 23
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Animal:

    def som(self):
        print("O animal faz um som genérico.")

class Cachorro(Animal):

    def som(self):
        print("O cachorro late.")

class Gato(Animal):

    def som(self):
        print("O gato miado.")

animal = Animal()

animal.som()

cachorro = Cachorro()

cachorro.som()

gato = Gato()

gato.som()
#
