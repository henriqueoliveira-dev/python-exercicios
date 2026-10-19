"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):

        self.velocidade += 10

        print(f"Velocidade atual: {self.velocidade} km/h")

    def frear(self):

        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f"Velocidade atual: {self.velocidade} km/h")

    def exibir_info(self):

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print("")


lista_carros = []


while True:

    print("")
    print("--- Menu ---")
    print("1. Adicionar Carro")
    print("2. Exibir informações dos carros")
    print("3. Acelerar Carro")
    print("4. Frear Carro")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")


    if escolha == "1":

        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")

        novo_carro = Carro(marca, modelo, cor)

        lista_carros.append(novo_carro)

        print("Carro adicionado com sucesso!")


    elif escolha == "2":

        if lista_carros:
            print("")
            print("Informações dos carros:")
            for carro in lista_carros:
                carro.exibir_info()
        else:
            print("Nenhum carro cadastrado.")


    elif escolha == "3":

        modelo = input("Digite o modelo do carro que deseja acelerar: ")

        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.acelerar()
                break
        else:
            print("Modelo não encontrado.")


    elif escolha == "4":

        modelo = input("Digite o modelo do carro que deseja frear: ")

        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.frear()
                break
        else:
            print("Modelo não encontrado.")

    elif escolha == "5":

        print("Saindo do programa. Até logo!")

        break

    else:
        print("Opção inválida. Tente novamente.")
