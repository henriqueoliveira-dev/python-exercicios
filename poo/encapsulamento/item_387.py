"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Mamifero:

    def __init__(self):

      print("Sou um Mamifero")

    def amamentar(self):

      print("Amamentando")

class Ave:

    def __init__(self):

      print("Sou uma Ave")

    def voar(self):

      print("Voando")

class Morcego(Mamifero, Ave):

    def __init__(self):

      Mamifero.__init__(self)
      Ave.__init__(self)

      print("Sou um Morcego")

    def emitir_som(self):
      print("Emitindo som de ecolocalização")

mamifero = Mamifero()
mamifero.amamentar()

ave = Ave()
ave.voar()

morcego = Morcego()
morcego.emitir_som()
