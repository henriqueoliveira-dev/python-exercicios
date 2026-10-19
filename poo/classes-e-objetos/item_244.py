"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 59
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# Alterado o nome da lista para evitar conflito com o nome da classe Produto
lista_produtos = []

with open('exercicio2.txt', 'r') as arquivo:
    for linha in arquivo:
      indice_separa = linha.index("R$")

      nome = linha[:indice_separa-1]
      # .strip() remove espaços em branco ou quebras de linha nas pontas
      valor = linha[indice_separa:].strip()
      produto = Produto(nome, valor)
      lista_produtos.append(produto)

for produto in lista_produtos:
  print(produto.nome, produto.valor)
