"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Animal:

    def falar(self):
        print("O animal está falando.")

class Cachorro(Animal):

    def falar(self):

        super().falar()
        print("O cachorro está latindo: Au au.")

animal = Animal()
#animal.falar()

cachorro = Cachorro()
cachorro.falar()
