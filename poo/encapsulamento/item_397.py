"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 26
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Veiculo:

    def mover(self):
        print("O veiculo está se movendo")


class Carro(Veiculo):

    def mover(self):
        print("O carro está se movendo em direção ao destino")

class Barco(Veiculo):

    def mover(self):
        print("O barco está se movendo em direção ao destino")

class Aviao(Veiculo):

    def mover(self):
        print("O avião está se movendo em direção ao destino")

veiculo = Veiculo()

veiculo.mover()

carro = Carro()

carro.mover()

barco = Barco()

barco.mover()

aviao = Aviao()

aviao.mover()

#
