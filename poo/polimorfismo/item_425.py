"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 54
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    Polimorfismo: Permitindo que um objeto se comporte de diferentes maneiras.
        - Polimorfismo de sobrescrita (também conhecido como overriding)

Polimorfismo de sobrescrita (ou "overriding" em inglês) é uma característica
de programação orientada a objetos onde uma subclasse fornece uma implementação
específica para um método que já é definido em sua superclasse. Esse mecanismo
permite que a subclasse herde características da superclasse mas também possa
modificar comportamentos específicos.
"""

"""
Exemplo: Classe Animal e suas subclasses Cachorro e Gato

Neste exemplo, vamos criar uma classe Animal com um método som. Em seguida,
vamos criar duas subclasses Cachorro e Gato que sobrescrevem o método som da
superclasse.
"""

# Classe Animal: Esta é a superclasse que define um comportamento básico
# comum a todos os animais.
class Animal:

    # Define um método chamado 'som' que imprime uma mensagem genérica indicando
    # que o animal faz um som.
    def som(self):
        print("O animal faz um som")

# Classe Cachorro: Esta é uma subclasse de Animal, ou seja, herda todos os
# métodos e atributos da classe Animal.
class Cachorro(Animal):

    # Sobrescreve o método 'som' da superclasse Animal. Isso significa que
    # este método substituirá o método da superclasse quando chamado em um
    # objeto da subclasse.
    def som(self):

        # Imprime uma mensagem específica que indica que o cachorro late, ao
        # invés de fazer um "som genérico".
        print("O cachorro late")


# Classe Gato: Esta é outra subclasse de Animal, herdando os métodos e atributos da classe Animal.
class Gato(Animal):

    # Sobrescreve o método 'som' da superclasse Animal. Este método substituirá o método da superclasse quando chamado em um objeto da subclasse Gato.
    def som(self):
        # Imprime uma mensagem específica indicando que o gato mia, diferentemente de fazer um "som genérico".
        print("O gato mia")

# Cria um objeto da classe Animal e armazena na variável 'animal'.
animal = Animal()

# Chama o método 'som' no objeto 'animal'. Este método é herdado da classe Animal.
# A saída será "O animal faz um som" porque estamos usando um objeto da classe Animal.
animal.som()  # Saída: "O animal faz um som"

# Cria um objeto da classe Cachorro e armazena na variável 'cachorro'.
cachorro = Cachorro()

# Chama o método 'som' no objeto 'cachorro'. Este método foi sobrescrito na classe Cachorro.
# A saída será "O cachorro late" porque estamos usando um objeto da classe Cachorro.
cachorro.som()  # Saída: "O cachorro late"

# Cria um objeto da classe Gato e armazena na variável 'gato'.
gato = Gato()

# Chama o método 'som' no objeto 'gato'. Este método foi sobrescrito na classe Gato.
# A saída será "O gato mia" porque estamos usando um objeto da classe Gato.
gato.som()  # Saída: "O gato mia"

"""
Note como cada subclasse (Cachorro e Gato) fornece sua própria
implementação do método som, sobrescrevendo o método som da superclasse
Animal. Este é um exemplo clássico de polimorfismo de sobrescrita. Quando
chamamos o método som em um objeto da subclasse, a implementação da subclasse
é a que é executada, e não a da superclasse.
"""
print()
