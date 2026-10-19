"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Retangulo:

    def __init__(self, largura, altura):

        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            print("Largura deve ser um valor positivo.")

    def altura(self):
        return self._altura

    @property
    def area(self):

        return self._largura * self._altura


r = Retangulo(5, 6)

print("Àrea:", r.area)

r.largura = 7

print("Nova area:", r.largura)
