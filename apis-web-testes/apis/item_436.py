"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class FormatadorDeFrase:

    def __init__(self, frase):
        self.frase = frase

    def para_maiusculas(self):
        self.frase = self.frase.upper()

    def para_minusculas(self):
        self.frase = self.frase.lower()

    def capitalizar(self):
        self.frase = self.frase.capitalize()

    def formato_titulo(self):
        self.frase = self.frase.title()

    def obter_frase(self):
        return self.frase

    def conta_vogais(self):

        vogais = 'aeiouáéíóúàèìòùãõê'

        contagem = 0

        frase_minuscula = self.frase.lower()
        for letra in frase_minuscula:

            if letra in vogais:

                contagem += 1

        return contagem

    def conta_consoantes(self):
        vogais = 'aeiouáéíóúàèìòùãõê' # Reutiliza a mesma definição de vogais para consistência
        contagem = 0
        frase_minuscula = self.frase.lower()
        for letra in frase_minuscula:
            # Conta a letra como consoante se for alfabética e não for uma vogal
            if letra.isalpha() and letra not in vogais:
                contagem += 1
        return contagem

    def conta_letra_a(self):
        print("")
        return self.frase.lower().count('a')

    def procurar_palavra(self, palavra):

        return self.frase.lower().count(palavra.lower())

    def obter_frase(self):
        return self.frase

def menu():

    print("\nBem-vindo ao Formatador de Frase!")

    frase = input("Digite uma frase: ")

    formatador = FormatadorDeFrase(frase)

    while True:

        print("\nEscolha uma opção para formatar sua frase:")
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Capitalizar a primeira letra")
        print("4. Converter para formato de título")
        print("5. Contar vogais")
        print("6. Contar consoantes")
        print("7. Contar ocorrências da letra 'a'")
        print("8. Procurar uma palavra")
        print("9. Obter a frase atual")
        print("0. Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":

            formatador.para_maiusculas()

            print("Frase atual:", formatador.obter_frase())

        elif escolha == "2":

            formatador.para_minusculas()
            print("Frase atual:", formatador.obter_frase())

        elif escolha == "3":

            formatador.capitalizar()
            print("Frase atual:", formatador.obter_frase())

        elif escolha == "4":

            formatador.formato_titulo()
            print("Frase atual:", formatador.obter_frase())

        elif escolha == "5":

            print(f"Total de vogais: {formatador.conta_vogais()}")

        elif escolha == "6":

            print(f"Total de Consoantes: {formatador.conta_consoantes()}")

        elif escolha == "7":

            print(f"Total de ocorrências da letra 'a': {formatador.conta_letra_a()}")


        elif escolha == "8":

            palavra = input("Digite a palavra que deseja procurar: ")

            contagem = formatador.procurar_palavra(palavra)

            if contagem > 0:
                print(f"A palavra '{palavra}' aparece {contagem} vezes(es) na frase.")
            else:
                print(f"A palavra '{palavra}' não foi encontrada na frase.")

        elif escolha == "9":

            print(f"Frase atual: {formatador.obter_frase()}")



        elif escolha == "0":

            print("Saindo do programa!")

            break

        else:
            print("Opção inválida. Tente novamente.")


        print(f"Frase atual: {formatador.obter_frase()}")


if __name__ == "__main__":
    menu()
