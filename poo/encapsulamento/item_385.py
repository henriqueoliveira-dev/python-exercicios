"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

#Solução

class Animal:

  def fazer_som(self):
      print("O animal faz um som.")


class Cachorro(Animal):

  def fazer_som(self):
      print("O cachorro faz woof-woof.")

  def latir(self):
      print("Woof-woof")

class Gato(Animal):

  def fazer_som(self):

      print("O gato faz miau.")

  def miar(self):
      print("Miau")

animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.fazer_som()
cachorro.fazer_som()
gato.fazer_som()

cachorro.latir()
gato.miar()
#
