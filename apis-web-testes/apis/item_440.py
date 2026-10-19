"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class ManipuladorDeLista:

  def __init__(self):

    self.lista = []

  def remover_elemento(self, elemento):
    try:
      self.lista.remove(elemento)
      print(f"Elemento {elemento} removido com sucesso!")

    except ValueError:
      print(f"Elemento {elemento} não encontrado na lista.")


  def adicionar_elemento(self, elemento):

    self.lista.append(elemento)


  def encontrar_maior(self):

      if self.lista:

         return max(self.lista)

      else:

        return "A lista está vazia"


  def encontrar_menor(self):

    if self.lista:

      return min(self.lista)

    else:

      return None


  def calcular_media(self):

    if self.lista:

      "\n"

      return sum(self.lista) / len(self.lista)

    else:

      return None


  def mostrar_lista(self):

      return self.lista


def menu():

    manipulador = ManipuladorDeLista()



    while True:

        print("\nEscolha uma opção: ")
        print("1. Adicionar elemneto")
        print("2. Remover elemneto")
        print("3. Encontrar maior elemento")
        print("4. Encontrar menor Elemento")
        print("5. Calcular Média")
        print("6. Mostrar lista")
        print("7. Sair")

        escolha = input("Digite um número da sua escolha: ")

        if escolha == "1":

            try:

                elemento = int(input("Digite o elemento que deseja adicionar: "))

                manipulador.adicionar_elemento(elemento)

                print(f"Elemento {elemento} adicionado com sucesso!")

            except ValueError:

                print("Entrada inválida. Por favor, insira um número inteiro.")

        if escolha == "2":

            try:

                elemento = int(input("Digite o elemento que deseja remover: "))

                manipulador.remover_elemento(elemento)

            except ValueError:

                print("Entrada inválida. Por favor, insira um número inteiro.")


        elif escolha == "3":

            print(f"O maior elemento é: {manipulador.encontrar_maior()}")


        elif escolha == "4":

            print(f"O menor elemento é: {manipulador.encontrar_menor()}")

        elif escolha == "5":

            print(f"A média dos elementos é: {manipulador.calcular_media()}")


        elif escolha == "6":

            print(f"Lista atual: {manipulador.mostrar_lista()}")

        elif escolha == "7":

            print("Saindo do programa!")

            break

        else:

            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
