"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 46
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Pilares da POO

    Herança: Criando novas classes a partir de classes existentes.
        Uso da função super().


A função super() em Python é usada para chamar um método da classe pai
dentro da classe derivada. Isso é útil quando você quer estender ou modificar
o comportamento de um método herdado sem substituí-lo completamente.

Vejamos um exemplo prático. Suponha que você tem uma classe Animal com um
método falar(). Você quer criar uma classe Cachorro que herda de Animal e
estende o método falar() para incluir um comportamento adicional.
"""


# Definindo uma classe chamada Animal, que servirá como a superclasse (classe pai).
class Animal:

    # Definindo um método chamado falar() dentro da classe Animal.
    def falar(self):

        # Quando o método falar() é chamado, ele imprime a string "O animal está falando".
        print("O animal está falando")

# Definindo uma classe chamada Cachorro, que herda da classe Animal (portanto, é uma subclasse).
class Cachorro(Animal):

    # Sobrescrevendo o método falar() da classe pai (Animal) na subclasse (Cachorro).
    def falar(self):

        # Chamando o método falar() da classe pai (Animal) usando super().
        # Isso é feito para que a subclasse também execute o comportamento da superclasse.
        super().falar()

        # Imprime uma string específica para a classe Cachorro.
        print("O cachorro diz: Au au")

# Criando uma instância da classe Animal e armazenando-a na variável 'animal'.
animal = Animal()

# Chamando o método falar() da classe Animal usando a instância 'animal'.
# Isso imprimirá "O animal está falando".
animal.falar()

# Criando uma instância da classe Cachorro e armazenando-a na variável 'cachorro'.
cachorro = Cachorro()

# Chamando o método falar() da classe Cachorro usando a instância 'cachorro'.
# Isso imprimirá "O animal está falando" e também "O cachorro diz: Au au" porque
# o método da superclasse também é chamado.
cachorro.falar()

# Saída:
# O animal está falando
# O cachorro diz: Au au

"""
No exemplo acima, o método falar() da classe Cachorro chama o
método falar() da classe pai Animal usando super().falar().

Isso assegura que o comportamento da classe pai seja preservado, e
então adiciona um comportamento adicional ("O cachorro diz: Au au").

Isso é particularmente útil em situações onde o método da classe pai é
complexo e você não quer reescrevê-lo completamente na classe filha.

Você simplesmente chama o método original com super() e adiciona o
comportamento adicional que você precisa.
"""
print()
