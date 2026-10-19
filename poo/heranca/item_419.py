"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 42
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    Tipos de Herança

            1. Herança Simples: Uma classe derivada de uma única classe base.
            2. Herança Múltipla: Uma classe derivada de mais de uma classe base.


2. Herança Múltipla: Uma classe derivada de mais de uma classe base.

Exemplo de herança múltipla em Python.

Vamos considerar duas classes base, Mamifero e Ave,
e uma classe derivada Morcego, que herda de ambas.
"""

# Classe base (ou classe pai) para representar mamíferos
class Mamifero:

    # Este é o método construtor (__init__), uma função especial em Python
    # que é automaticamente chamada quando um novo objeto dessa classe é criado.
    def __init__(self):

        # Este print é apenas um marcador para nos ajudar a identificar quando um objeto desta classe é criado.
        print("Sou um mamífero")

    # Este é um método de instância chamado 'amamentar'. Os métodos de instância são funções
    # que operam em um objeto e podem acessar/alterar os atributos do objeto e chamar outros métodos do objeto.
    def amamentar(self):

        # Novamente, este print é mais um marcador para fins de demonstração.
        print("Amamentando...")

# Definição da classe Ave, que será a classe base (ou classe pai) para representar todas as aves.
class Ave:

    # Método construtor da classe Ave. Este método é invocado automaticamente quando um novo
    # objeto desta classe é criado.
    # Ele não aceita parâmetros além de 'self', que é uma referência ao objeto em si.
    def __init__(self):

        # Imprime uma mensagem no terminal para indicar que um objeto da classe Ave foi criado.
        print("Sou uma ave")

    # Definição de um método de instância chamado 'voar'.
    # Os métodos de instância podem acessar ou modificar atributos do objeto e também podem
    # chamar outros métodos do objeto.
    def voar(self):

        # Imprime uma mensagem no terminal para simular o ato de voar.
        print("Voando...")


# Classe Morcego, que é uma classe derivada (ou classe filha) de duas classes pais: Mamifero e Ave.
# Este é um exemplo de herança múltipla, onde uma classe deriva de mais de uma classe base.
class Morcego(Mamifero, Ave):

    # Método construtor da classe Morcego.
    # Este método é chamado automaticamente quando um novo objeto da classe Morcego é criado.
    def __init__(self):

        # Chamada explícita ao construtor da classe pai Mamifero.
        # Isso é feito para inicializar qualquer lógica ou atributos específicos da classe Mamifero.
        Mamifero.__init__(self)

        # Chamada explícita ao construtor da classe pai Ave.
        # Isso é feito para inicializar qualquer lógica ou atributos específicos da classe Ave.
        Ave.__init__(self)

        # Imprime uma mensagem para indicar que um objeto da classe Morcego foi criado.
        # Note que esta linha é executada após as chamadas aos construtores das classes pais.
        print("Sou um morcego")

    # Definição de um novo método específico para a classe Morcego, chamado 'emitir_som'.
    # Este método simula o morcego emitindo sons para ecolocalização, uma característica
    # única de alguns morcegos.
    def emitir_som(self):

        # Imprime uma mensagem para simular o morcego emitindo sons de ecolocalização.
        print("Emitindo som de ecolocalização...")


# Criando um objeto da classe Morcego para testar seus métodos
morcego = Morcego()

# Chamando o método amamentar(), que é herdado da classe Mamifero
morcego.amamentar()

# Chamando o método voar(), que é herdado da classe Ave
morcego.voar()

# Chamando o método emitir_som(), que é específico da classe Morcego
morcego.emitir_som()
