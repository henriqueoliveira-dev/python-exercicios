"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
2. Conceitos Básicos

    Atributos: Definindo e acessando atributos de uma classe.

"""

#Exemplo Prático: Gerenciamento de Jogadores em um Time de Futebol

#Descrição:

#Imagine que você está desenvolvendo um software simples para gerenciar
#jogadores em um time de futebol. Cada jogador tem um nome, posição, número
#da camisa e quantidade de gols marcados na temporada.

#1. Definição da Classe Jogador:

# Define a classe Jogador
class Jogador:

    # Método construtor da classe
    def __init__(self, nome, posicao, numero_camisa, gols=0):

        self.nome = nome              # Atribui o valor do parâmetro 'nome' ao atributo 'nome' do objeto
        self.posicao = posicao        # Atribui o valor do parâmetro 'posicao' ao atributo 'posicao' do objeto
        self.numero_camisa = numero_camisa  # Atribui o valor do parâmetro 'numero_camisa' ao atributo 'numero_camisa' do objeto
        self.gols = gols              # Atribui o valor do parâmetro 'gols' ao atributo 'gols' do objeto (com valor padrão 0 se não for fornecido)


#2. Instanciando e Acessando Atributos:

# Instanciando jogadores

# Cria uma nova instância da classe Jogador com os atributos
# nome="Roberto", posicao="Atacante" e numero_camisa=9
jogador1 = Jogador("Roberto", "Atacante", 9)

# Cria uma nova instância da classe Jogador com os atributos
# nome="Carlos", posicao="Goleiro" e numero_camisa=1
jogador2 = Jogador("Carlos", "Goleiro", 1)


# Acessando atributos

# Utiliza a função print para mostrar os atributos nome, posicao e
# numero_camisa do jogador1 em um formato legível
print(f"{jogador1.nome} é um {jogador1.posicao} e usa a camisa número {jogador1.numero_camisa}.")

# Utiliza a função print para mostrar os atributos nome, posicao e
# numero_camisa do jogador2 em um formato legível
print(f"{jogador2.nome} é um {jogador2.posicao} e usa a camisa número {jogador2.numero_camisa}.")


# Suponha que Roberto marcou um gol, vamos atualizar o atributo gols dele

# Incrementa em 1 o número de gols do jogador1 (Roberto)
jogador1.gols += 1

# Incrementa novamente em 1 o número de gols do jogador1 (Roberto)
jogador1.gols += 1

# Mais um incremento de 1 gol para jogador1 (Roberto)
jogador1.gols += 1

# Continua incrementando o número de gols de jogador1 (Roberto)
jogador1.gols += 1

# E mais uma vez, incrementa em 1 o número de gols de jogador1 (Roberto)
jogador1.gols += 1


# Utiliza a função print para mostrar os atributos nome, posicao e
# numero_camisa do jogador1 em um formato legível
# Utiliza a função print para mostrar a quantidade de gols que jogador1 (Roberto) marcou na temporada
print(f"{jogador1.nome} marcou {jogador1.gols} gol(s) nesta temporada.")


"""
O exemplo acima ajuda a entender como definir atributos em uma classe,
como instanciar objetos dessa classe e como acessar e modificar esses atributos
diretamente.
"""
print()
