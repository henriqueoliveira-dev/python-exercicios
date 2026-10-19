"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
Exercício - Informações de Frutas em uma Mercearia

Em uma mercearia, várias frutas são vendidas, e você deseja criar um
sistema simples para gerenciar as informações sobre essas frutas.

Objetivos:

    1. Definir uma classe chamada Fruta.
    2. Instanciar um ou mais objetos desta classe.
    3. Acessar e exibir os atributos dos objetos instanciados.

Instruções:

    1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).

    2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:

        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]

"""


#Solução:

"""
 1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).
"""
# Definindo a classe Fruta
class Fruta:

    # Método inicializador da classe Fruta
    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):

        self.nome = nome  # Atribui o valor do parâmetro 'nome' ao atributo 'nome' da instância
        self.preco_por_kg = preco_por_kg  # Atribui o valor do parâmetro 'preco_por_kg' ao atributo 'preco_por_kg' da instância
        self.quantidade_em_estoque = quantidade_em_estoque  # Atribui o valor do parâmetro 'quantidade_em_estoque' ao atributo 'quantidade_em_estoque' da instância

    """
    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:

        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]
    """

    # Definição do método para exibir informações da fruta
    def exibir_info(self):

        # Imprime o nome da fruta, acessando o atributo 'nome' da instância atual
        print(f"Nome da Fruta: {self.nome}")

        # Imprime o preço por Kg da fruta, formatando para duas casas decimais
        print(f"Preço por Kg: R${self.preco_por_kg:.2f}")

        # Imprime a quantidade em estoque da fruta, acessando o atributo 'quantidade_em_estoque' da instância atual
        print(f"Quantidade em Estoque: {self.quantidade_em_estoque}kg")



# 2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

# Instanciando duas frutas diferentes
maca = Fruta("Maçã", 2.5, 10)
banana = Fruta("Banana", 1.8, 15)

maca.exibir_info()
print("-------------")
banana.exibir_info()
