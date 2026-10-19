"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
2. Conceitos Básicos

    Classes e Objetos: Definindo e instanciando classes.
"""

#Vamos começar com um exemplo simples de uma classe chamada Carro.
#Esta classe irá representar um carro genérico e terá algumas propriedades e métodos.


# Definindo a classe Carro
# Definindo uma classe chamada Carro
class Carro:

    # Método inicializador (construtor) da classe que é invocado quando um objeto
    # da classe é criado
    def __init__(self, marca, modelo, cor):
        self.marca = marca      # Define o atributo marca do carro com o valor fornecido
        self.modelo = modelo    # Define o atributo modelo do carro com o valor fornecido
        self.cor = cor          # Define o atributo cor do carro com o valor fornecido
        self.velocidade = 0     # Inicializa o atributo velocidade atual do carro com 0


    # Método que aumenta a velocidade do carro em 10 km/h
    def acelerar(self):

        # Incrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade + 10
        self.velocidade += 10

        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")

    # Método que diminui a velocidade do carro em 10 km/h
    def frear(self):

        # Decrementa a velocidade atual em 10 km/h
        # self.velocidade = self.velocidade - 10
        self.velocidade -= 10

        # Garante que a velocidade não se torne negativa
        if self.velocidade < 0:
            self.velocidade = 0

        # Exibe a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade} km/h")

    # Método que exibe as informações básicas do carro
    def exibir_info(self):

        # Exibe a marca, modelo e cor do carro
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")


# Instanciando objetos da classe Carro
carro1 = Carro("Toyota", "Corolla", "Branco")

carro1.exibir_info()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()

# Instanciando objetos da classe Carro
carro2 = Carro("Ford", "Fiesta", "Azul")

print("\n -------- \n")

carro2.exibir_info()
carro2.acelerar()
carro2.acelerar()
carro2.frear()

"""
No exemplo acima:

    - A classe Carro é definida com atributos como marca, modelo,
    cor e velocidade. Ela também tem métodos como acelerar, frear e exibir_info.

    - O método __init__ é o construtor da classe, que é chamado automaticamente
    quando criamos uma nova instância da classe.

    - Criamos duas instâncias (objetos) dessa classe: carro1 e carro2, com diferentes atributos.

    - Em seguida, chamamos alguns métodos nesses objetos para demonstrar seu funcionamento.

    - O self é um parâmetro convencional utilizado em muitos métodos de classes em Python
    para se referir à própria instância do objeto. É equivalente ao this em muitas outras linguagens de programação.

    - O prefixo self. é usado para diferenciar entre atributos de instância e variáveis locais.
    Sem o self, a variável seria interpretada como uma variável local.

A Programação Orientada a Objetos permite organizar o código de forma que
dados (atributos) e comportamentos (métodos) estejam agrupados em classes, facilitando
a manutenção, extensão e compreensão do código.
"""
print()
