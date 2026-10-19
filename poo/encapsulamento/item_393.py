"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 20
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Impressora:

    def imprimir(sel, dado):

        if isinstance(dado, str):
            print(f"Imprimindo texto: {dado}")

        elif isinstance(dado, list):
             print("Imprimindo lista de textos")

             for item in dado:
                print(f"- {item}")

        elif isinstance(dado, dict):
            print("Imprimindo dicionário de textos")

            for chave, valor in dado.items():
                print(f"{chave}: {valor}")

        else:

            print("Tipo de dado não suportado para impressão.")

#Testando a classe

impressora = Impressora()

impressora.imprimir("Olá, mundo!")
print("")
impressora.imprimir(["item1", "item2", "item3"])
impressora.imprimir({"chave1": "valor1", "chave2": "valor2"})
impressora.imprimir(123)
#
