"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 52
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício: Polimorfismo de "Sobrecarga" com a Classe Impressora

O objetivo deste exercício é criar uma classe Impressora que possa
imprimir dados de tipos diferentes: texto, lista de textos e dicionário
de textos. Para isso, implementaremos um método imprimir que se comporta
de forma diferente, dependendo do tipo de dado passado como argumento.

    Passo 1: Implemente a Classe Impressora

        Crie uma classe Impressora com um método imprimir que
        aceita um único argumento. Dentro do método, utilize if e isinstance
        para verificar o tipo do argumento e decidir como imprimi-lo.


    Passo 2: Teste a Classe

        Após implementar a classe, crie uma instância da Impressora
        e chame o método imprimir com diferentes tipos de argumentos.
"""

#Solução:

"""
Passo 1: Implemente a Classe Impressora

        Crie uma classe Impressora com um método imprimir que
        aceita um único argumento. Dentro do método, utilize if e isinstance
        para verificar o tipo do argumento e decidir como imprimi-lo.
"""

"""
A função isinstance() é uma função embutida em Python usada
para verificar se um objeto é uma instância de uma classe específica
ou de uma subclasse dessa classe. Ela também pode ser usada para verificar
se um objeto é uma instância de qualquer uma das classes especificadas como uma tupla.
"""

# Define a classe Impressora
class Impressora:

    # Define o método imprimir, que aceita um único argumento chamado 'dado'.
    def imprimir(self, dado):

        # Verifica se o argumento 'dado' é uma string (str).
        if isinstance(dado, str):

            # Se for uma string, imprime o texto, precedido pela mensagem "Imprimindo texto:".
            print(f"Imprimindo texto: {dado}")

        # Se 'dado' não for uma string, verifica se é uma lista (list).
        elif isinstance(dado, list):

            # Se for uma lista, imprime a mensagem "Imprimindo lista de textos:".
            print("Imprimindo lista de textos:")

            # Itera sobre cada item da lista 'dado'.
            for item in dado:

                # Imprime cada item da lista, precedido por um traço e um espaço.
                print(f" - {item}")

        # Se 'dado' não for uma string nem uma lista, verifica se é um dicionário (dict).
        elif isinstance(dado, dict):

            # Se for um dicionário, imprime a mensagem "Imprimindo dicionário de textos:".
            print("Imprimindo dicionário de textos:")

            # Itera sobre cada par chave-valor no dicionário 'dado'.
            for chave, valor in dado.items():

                # Imprime cada par chave-valor, formatado como "chave: valor".
                print(f" - {chave}: {valor}")

        # Se 'dado' não for uma string, uma lista, nem um dicionário.
        else:

            # Imprime a mensagem indicando que o tipo de dado não é suportado para impressão.
            print("Tipo de dado não suportado para impressão")

"""
Passo 2: Teste a Classe

        Após implementar a classe, crie uma instância da Impressora
        e chame o método imprimir com diferentes tipos de argumentos.
"""

# Criando uma instância da classe Impressora e armazenando-a na variável 'impressora'.
impressora = Impressora()

# Chamando o método 'imprimir' na instância 'impressora' e passando uma string como argumento.
# Isso deve imprimir "Imprimindo texto: Olá, mundo!" porque o método
# identificará que o tipo de dado é uma string.
impressora.imprimir("Olá, mundo!")

# Chamando o método 'imprimir' na instância 'impressora' e passando uma
# lista de strings como argumento.
# Isso deve imprimir "Imprimindo lista de textos:" seguido pelos elementos da
# lista, porque o método identificará que o tipo de dado é uma lista.
impressora.imprimir(["Olá", "mundo", "!"])

# Chamando o método 'imprimir' na instância 'impressora' e passando um dicionário como argumento.
# Isso deve imprimir "Imprimindo dicionário de textos:" seguido pelos pares chave-valor do
# dicionário, porque o método identificará que o tipo de dado é um dicionário.
impressora.imprimir({"saudacao": "Olá", "objeto": "mundo"})

# Chamando o método 'imprimir' na instância 'impressora' e passando um número inteiro como argumento.
# Isso deve imprimir "Tipo de dado não suportado para impressão" porque o método identificará
# que o tipo de dado não é uma string, lista ou dicionário.
impressora.imprimir(42)


"""
Neste exercício, você viu como um único método pode ser projetado
para lidar com diferentes tipos de dados, algo semelhante ao que
poderia ser alcançado com polimorfismo de sobrecarga em outras
linguagens de programação.

Aqui, usamos condicionais e a função isinstance para alcançar
esse comportamento em Python.
"""
print()
