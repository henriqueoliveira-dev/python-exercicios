"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 34
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício: Termômetro Digital

Você vai criar uma classe Termometro que representará um termômetro
digital simples.

Requisitos:

    1. O termômetro deve ter um atributo protegido _temperatura que
        armazena a temperatura atual em graus Celsius.

    2. Implemente um método getter usando @property para a temperatura.

    3. Implemente um método setter para a temperatura que verifica se o
        valor é uma temperatura razoável para a atmosfera terrestre (digamos, entre -100°C e 100°C).

Exemplo de Uso:

t = Termometro()
t.temperatura = 25
print(t.temperatura)  # Deve imprimir 25

t.temperatura = 200  # Deve imprimir "Temperatura fora do alcance"
print(t.temperatura)  # Deve imprimir 25, pois a temperatura anterior não foi alterada


Sua tarefa é implementar essa classe Termometro e garantir que ela funcione como especificado.
"""

#Solução

# Definindo a classe Termometro para representar um termômetro digital simples
class Termometro:

    """
    1. O termômetro deve ter um atributo protegido _temperatura que
        armazena a temperatura atual em graus Celsius.
    """
    # Método construtor para inicializar a instância da classe
    def __init__(self):

        # Inicializando um atributo protegido '_temperatura' com o valor 0
        # Este atributo armazena a temperatura atual em graus Celsius
        self._temperatura = 0

    """
    2. Implemente um método getter usando @property para a temperatura.
    """
    # Utilizando o decorador @property para indicar que o método a seguir
    # será o 'getter' para o atributo temperatura
    @property
    def temperatura(self):

        # Este método retorna o valor atual do atributo protegido '_temperatura'
        return self._temperatura

    """
    3. Implemente um método setter para a temperatura que verifica se o
        valor é uma temperatura razoável para a atmosfera terrestre (digamos, entre -100°C e 100°C).
    """

    # Utilizando o decorador @temperatura.setter para indicar que o método a seguir
    # será o 'setter' para o atributo temperatura
    @temperatura.setter
    def temperatura(self, valor):

        # Este bloco de código verifica se o valor fornecido para a temperatura
        # está dentro do intervalo de -100 a 100 graus Celsius
        if -100 <= valor <= 100:

            # Se o valor estiver dentro do intervalo, atualizamos o atributo
            # protegido '_temperatura' com o novo valor
            self._temperatura = valor
        else:

            # Se o valor estiver fora do intervalo permitido, imprimimos uma mensagem de erro
            print("Temperatura fora do alcance")


# Testando a classe Termometro
t = Termometro()
t.temperatura = 25  # Configurando a temperatura para 25°C
print(t.temperatura)  # Deve imprimir 25

t.temperatura = 200  # Tentando definir uma temperatura fora do alcance
print(t.temperatura)  # Deve imprimir 25, pois a tentativa anterior deveria ter falhado e a temperatura não foi alterada
