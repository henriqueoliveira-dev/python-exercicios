"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False

    def acordar(self):
        if self.acordado:
          print(f"{self.nome} já está acordado.")
        else:
          self.acordado = True

          print(f"{self.nome} acordou.")

    def comer(self):

        if self.dirigindo:
            print(f"{self.nome} não pode comer enquanto está dirigindo.")

        elif not self.acordado:
            print(f"{self.nome} não pode comer enquanto está dormindo.")

        elif self.comendo:
            print(f"{self.nome} já está comendo.")

        else:
            self.comendo = True
            print(f"{self.nome} está comendo.")

    def parar_de_comer(self):
        if not self.comendo:

          print(f"{self.nome} não está comendo no momento")

        else:

          self.comendo = False
          print(f"{self.nome} Terminou de Comer.")

joao = Pessoa("João")

joao.acordar()
joao.acordar()

joao.comer()

joao.comer()

joao.parar_de_comer()

joao.parar_de_comer()
