"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 56
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício: Polimorfismo de Sobrescrita com Classes de Veículos

O objetivo deste exercício é entender o polimorfismo de
sobrescrita (overriding) através de um exemplo prático envolvendo
diferentes tipos de veículos. Cada tipo de veículo pode ter uma forma
específica de movimento, que é descrita pelo método mover.

    Passo 1: Implemente a Classe Veiculo

        Crie uma classe chamada Veiculo que terá um método chamado
        mover. Este método imprimirá uma mensagem genérica sobre como
        um veículo se move.

    Passo 2: Implemente as Subclasses Carro, Barco e Aviao

        Agora crie três subclasses: Carro, Barco e Aviao. Cada uma
        dessas subclasses deve sobrescrever o método mover para fornecer
        detalhes específicos sobre como cada tipo de veículo se move.

    Passo 3: Teste as Classes

        Depois de implementar as subclasses, crie instâncias
        de cada uma e chame o método mover.
"""

#Solução:

"""
Passo 1: Implemente a Classe Veiculo

        Crie uma classe chamada Veiculo que terá um método chamado
        mover. Este método imprimirá uma mensagem genérica sobre como
        um veículo se move.
"""

# Classe Veiculo: Esta é uma classe geral que define o comportamento
# básico de um veículo.
class Veiculo:

    # Define um método chamado 'mover', que imprimirá uma mensagem genérica
    # indicando que o veículo está se movendo.
    def mover(self):
        print("O veículo está se movendo")


"""
Passo 2: Implemente as Subclasses Carro, Barco e Aviao

        Agora crie três subclasses: Carro, Barco e Aviao. Cada uma
        dessas subclasses deve sobrescrever o método mover para fornecer
        detalhes específicos sobre como cada tipo de veículo se move.
"""

# Classe Carro: Esta é uma subclasse da classe Veiculo e herda os métodos e
# atributos da classe Veiculo.
class Carro(Veiculo):

    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer um
    # comportamento específico para Carro.
    def mover(self):

        # Imprime uma mensagem específica indicando que o carro está dirigindo na estrada.
        print("O carro está dirigindo na estrada")

# Classe Barco: Esta é outra subclasse da classe Veiculo e também herda
# os métodos e atributos da classe Veiculo.
class Barco(Veiculo):

    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer um
    # comportamento específico para Barco.
    def mover(self):

        # Imprime uma mensagem específica indicando que o barco está navegando no mar.
        print("O barco está navegando no mar")

# Classe Aviao: Esta é outra subclasse da classe Veiculo e, mais uma
# vez, herda os métodos e atributos da classe Veiculo.
class Aviao(Veiculo):

    # Sobrescreve o método 'mover' da superclasse Veiculo para fornecer
    # um comportamento específico para Aviao.
    def mover(self):

        # Imprime uma mensagem específica indicando que o avião está voando no céu.
        print("O avião está voando no céu")


"""
Passo 3: Teste as Classes

        Depois de implementar as subclasses, crie instâncias
        de cada uma e chame o método mover.
"""

# Instanciando objetos de cada classe e subclasse
# Cria um objeto da classe Veiculo e armazena na variável 'veiculo'.
veiculo = Veiculo()

# Cria um objeto da classe Carro (subclasse de Veiculo) e armazena na variável 'carro'.
carro = Carro()

# Cria um objeto da classe Barco (subclasse de Veiculo) e armazena na variável 'barco'.
barco = Barco()

# Cria um objeto da classe Aviao (subclasse de Veiculo) e armazena na variável 'aviao'.
aviao = Aviao()

# Chamando o método mover para cada objeto
# Chama o método 'mover' no objeto 'veiculo'. Este método é herdado da classe Veiculo.
# A saída será "O veículo está se movendo" porque estamos usando um objeto da classe Veiculo.
veiculo.mover()  # Saída: "O veículo está se movendo"

# Chama o método 'mover' no objeto 'carro'. Este método foi sobrescrito na classe Carro.
# A saída será "O carro está dirigindo na estrada" porque estamos usando um objeto da classe Carro.
carro.mover()    # Saída: "O carro está dirigindo na estrada"

# Chama o método 'mover' no objeto 'barco'. Este método foi sobrescrito na classe Barco.
# A saída será "O barco está navegando no mar" porque estamos usando um objeto da classe Barco.
barco.mover()    # Saída: "O barco está navegando no mar"

# Chama o método 'mover' no objeto 'aviao'. Este método foi sobrescrito na classe Aviao.
# A saída será "O avião está voando no céu" porque estamos usando um objeto da classe Aviao.
aviao.mover()    # Saída: "O avião está voando no céu"


"""
Observe como o método mover foi sobrescrito em cada
subclasse (Carro, Barco, Aviao) para fornecer uma implementação
específica de como o veículo se move, demonstrando assim o
conceito de polimorfismo de sobrescrita.
"""
print()
