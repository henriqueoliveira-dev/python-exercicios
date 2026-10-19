"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 18
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Calculadora:

    def somar(self, num1, num2, num3=None):

        if num3 is not None:
            return num1 + num2 + num3

        else:
            return num1 + num2

calculadora = Calculadora()

print(calculadora.somar(2, 3))
print(calculadora.somar(2, 3, 4))
