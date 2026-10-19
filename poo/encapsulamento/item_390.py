"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 16
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def exibir_info(self):
        super().exibir_info()
        print(f"Cor: {self.cor}")

veiculo1 = Veiculo("Toyota","Corolla")

veiculo1.exibir_info()
print('')
carro1 = Carro("Toyota", "Corolla", "Vermelho")

carro1.exibir_info()
#
