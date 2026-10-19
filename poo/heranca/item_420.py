"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 44
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
Exercício: A Classe MusicoAtleta

Você está criando um software para uma competição muito especial
que envolve múltiplas disciplinas: música e esportes.

Você foi instruído a criar classes que representem um Musico, um Atleta, e um
MusicoAtleta que herda características de ambos.

    1. A classe Musico deve ter um método tocar_instrumento que
        imprime "Tocando instrumento musical".

    2. A classe Atleta deve ter um método correr que imprime "Correndo na pista".

    3. A classe MusicoAtleta deve herdar de ambas as classes, Musico e Atleta.

    4. A classe MusicoAtleta deve também ter um método próprio chamado
        exibir_habilidades, que imprime "Tocando instrumento e correndo".

Crie instâncias das classes e teste os métodos para garantir que a
herança múltipla esteja funcionando como esperado.

A ideia aqui é praticar o conceito de herança múltipla, fazendo com que uma classe
herde atributos e métodos de duas classes pai diferentes.
"""

#Solução


"""
 1. A classe Musico deve ter um método tocar_instrumento que
        imprime "Tocando instrumento musical".
"""
# Definindo a classe Musico, que será uma das classes pai (ou "superclasse")
class Musico:

    # Definindo o método tocar_instrumento, que será uma habilidade específica dos músicos
    def tocar_instrumento(self):

        # Ação que será realizada quando o método for chamado
        print("Tocando instrumento musical")


# 2. A classe Atleta deve ter um método correr que imprime "Correndo na pista".

# Definindo a classe Atleta, que será a outra classe pai (ou "superclasse")
class Atleta:

    # Definindo o método correr, que será uma habilidade específica dos atletas
    def correr(self):

        # Ação que será realizada quando o método for chamado
        print("Correndo na pista")


# 3. A classe MusicoAtleta deve herdar de ambas as classes, Musico e Atleta.

# Definindo a classe MusicoAtleta, que herda tanto de Musico quanto de Atleta
# Este é um exemplo de herança múltipla
class MusicoAtleta(Musico, Atleta):


    """
    4. A classe MusicoAtleta deve também ter um método próprio chamado
        exibir_habilidades, que imprime "Tocando instrumento e correndo".
    """
    # Método específico dessa classe filha para exibir ambas as habilidades
    def exibir_habilidades(self):

        # Ação que será realizada quando o método for chamado
        print("Tocando instrumento e correndo")


# Criando um objeto da classe MusicoAtleta, que herda métodos de ambas as classes pai
musico_atleta = MusicoAtleta()

# Testando o método tocar_instrumento, herdado da classe Musico
musico_atleta.tocar_instrumento()  # A saída será: "Tocando instrumento musical"

# Testando o método correr, herdado da classe Atleta
musico_atleta.correr()  # A saída será: "Correndo na pista"

# Testando o método exibir_habilidades, específico da classe MusicoAtleta
musico_atleta.exibir_habilidades()  # A saída será: "Tocando instrumento e correndo"
