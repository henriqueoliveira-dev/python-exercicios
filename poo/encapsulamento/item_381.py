"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 5
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Pet:

    def __init__(self):

        self._nome = ""
        self._idade = 0
        self._peso = 0

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):

        if isinstance(novo_nome, str) and novo_nome != "":
            self._nome = novo_nome

        else:
            print("Nome inválido.")

    def get_peso(self):
        return self._peso

    def set_peso(self, novo_peso):

        if isinstance(novo_peso, float) and novo_peso > 0:
            self._peso = novo_peso

        else:
            print("Peso inválido.")

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):

        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade

        else:
            print("Idade inválida.")

    def exibir_info(self):

        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} kg")

def mostra_menu():

    print("\n---- Menu de Gerenciamento de Pet ----")
    print("")
    print("1. Definir o nome do pet")
    print("2. Definir a idade do pet")
    print("3. Definir o peso do pet")
    print("4. Exibir informações do pet")
    print("5. Sair")
    print("---------------------------------------")

    escolha = input("Escolha uma opção: ")

    return escolha

def main():
    meu_pet = Pet()

    while True:
        escolha = mostra_menu()

        if escolha == "1":
            nome = input("Digite o novo nome do pet: ")
            meu_pet.set_nome(nome)

        elif escolha == "2":

          try:
            idade = int(input("Digite a nova idade do pet: "))
            meu_pet.set_idade(idade)

          except ValueError:
            print("A idade deve ser um número inteiro.")

        elif escolha == "3":

          try:
            peso = float(input("Digite o novo peso do pet: "))
            meu_pet.set_peso(peso)

          except ValueError:
            print("Peso inválido. Por vaor, digite um número válido.")

        elif escolha == "4":
            meu_pet.exibir_info()

        elif escolha == "5":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()
