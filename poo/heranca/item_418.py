"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 40
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
Exercício Herança Simples:

Crie uma classe Animal que tenha um método fazer_som().
Essa classe será a classe pai para outras duas classes: Cachorro e Gato.

Ambas as classes filhas deverão ter seus próprios métodos fazer_som() que
sobrescrevem o método da classe pai. Além disso, a classe Cachorro
deve ter um método latir() e a classe Gato um método miar().

    1. A classe Animal deve ter um método fazer_som() que imprime "O animal faz um som".
    2. A classe Cachorro deve ter um método fazer_som() que imprime "O cachorro faz woof-woof".
    3. A classe Gato deve ter um método fazer_som() que imprime "O gato faz miau".
    4. A classe Cachorro deve ter um método adicional chamado latir() que imprime "Woof-woof".
    5. A classe Gato deve ter um método adicional chamado miar() que imprime "Miau".

Crie objetos das classes Cachorro e Gato e chame seus métodos para
testar se tudo está funcionando como esperado.
"""

#Solução

# 1. A classe Animal deve ter um método fazer_som() que imprime "O animal faz um som".

# Definindo uma classe Animal que atuará como classe pai (ou classe base)
class Animal:

    # Definindo um método chamado fazer_som dentro da classe Animal
    def fazer_som(self):

        print("O animal faz um som")  # Imprime uma mensagem padrão para qualquer animal

#---------------------------------------------------------------------

# 2. A classe Cachorro deve ter um método fazer_som() que imprime "O cachorro faz woof-woof".

# Definindo uma classe Cachorro que herda da classe Animal
class Cachorro(Animal):

    # Sobrescrevendo o método fazer_som para a classe Cachorro
    def fazer_som(self):

        print("O cachorro faz woof-woof")  # Imprime um som específico para cachorros

    # 4. A classe Cachorro deve ter um método adicional chamado latir() que imprime "Woof-woof".

    # Definindo um método adicional específico para a classe Cachorro
    def latir(self):

        print("Woof-woof")  # Imprime o som de um cachorro latindo


#---------------------------------------------------------------------

# 3. A classe Gato deve ter um método fazer_som() que imprime "O gato faz miau".

# Definindo uma classe Gato que também herda da classe Animal
class Gato(Animal):

    # Sobrescrevendo o método fazer_som para a classe Gato
    def fazer_som(self):

        print("O gato faz miau")  # Imprime um som específico para gatos

    # 5. A classe Gato deve ter um método adicional chamado miar() que imprime "Miau".

    # Definindo um método adicional específico para a classe Gato
    def miar(self):

        print("Miau")  # Imprime o som de um gato miando


# Criando um objeto da classe Animal e testando o seu método fazer_som
animal = Animal()

# Deverá imprimir "O animal faz um som", pois estamos usando o método da classe Animal
animal.fazer_som()

# Criando um objeto da classe Cachorro e testando os seus métodos
cachorro = Cachorro()

# Deverá imprimir "O cachorro faz woof-woof", pois estamos usando o método sobrescrito na classe Cachorro
cachorro.fazer_som()

# Deverá imprimir "Woof-woof", usando o método específico da classe Cachorro
cachorro.latir()

# Criando um objeto da classe Gato e testando os seus métodos
gato = Gato()

# Deverá imprimir "O gato faz miau", pois estamos usando o método sobrescrito na classe Gato
gato.fazer_som()

# Deverá imprimir "Miau", usando o método específico da classe Gato
gato.miar()
