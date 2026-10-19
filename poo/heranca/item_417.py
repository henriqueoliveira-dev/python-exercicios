"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 38
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    Tipos de Herança

            1. Herança Simples: Uma classe derivada de uma única classe base.
            2. Herança Múltipla: Uma classe derivada de mais de uma classe base.


1. Herança Simples: Uma classe derivada de uma única classe base.

A herança simples é um conceito de programação orientada
a objetos onde uma classe herda atributos e métodos de uma única
classe pai.

Vamos criar um exemplo simples de herança que representa diferentes
papéis em uma escola: Pessoa, Estudante e Professor.

A classe Pessoa é a classe pai e contém atributos e métodos comuns
a todas as pessoas em uma escola, como nome e idade.

As classes Estudante e Professor herdam da classe Pessoa e adicionam
atributos e métodos específicos para estudantes e professores, respectivamente.

Aqui está o código:
"""

# Classe base (ou classe pai) chamada Pessoa.
# Ela servirá como o modelo genérico para criar outras classes relacionadas.
class Pessoa:

    # Método construtor da classe Pessoa para inicializar os atributos nome e idade.
    def __init__(self, nome, idade):

        # Atribui o valor do argumento 'nome' ao atributo 'nome' da instância.
        self.nome = nome

        # Atribui o valor do argumento 'idade' ao atributo 'idade' da instância.
        self.idade = idade

    # Método para exibir informações sobre a Pessoa.
    def exibir_info(self):

        # Imprime as informações da Pessoa.
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Classe derivada (ou classe filha) chamada Estudante, que herda atributos e métodos
# da classe Pessoa.
class Estudante(Pessoa):

    # Método construtor da classe Estudante para inicializar os atributos nome,
    # idade e matricula.
    def __init__(self, nome, idade, matricula):

        # Chama o método construtor da classe pai (Pessoa) explicitamente.
        Pessoa.__init__(self, nome, idade)

        # Atributo específico para Estudante.
        self.matricula = matricula

    # Método para simular a ação de estudar.
    def estudar(self):

        # Imprime a ação de estudar.
        print(f"{self.nome} está estudando.")


# Classe derivada (ou classe filha) chamada Professor,
# que também herda atributos e métodos da classe Pessoa.
class Professor(Pessoa):

    # Método construtor para a classe Professor.
    def __init__(self, nome, idade, disciplina):

        # Chama o método construtor da classe pai (Pessoa) explicitamente.
        Pessoa.__init__(self, nome, idade)

        # Atributo específico para Professor.
        self.disciplina = disciplina

    # Método para simular a ação de ensinar.
    def ensinar(self):

        # Imprime a ação de ensinar.
        print(f"{self.nome} está ensinando {self.disciplina}.")


# Criação de objetos

# Cria um objeto da classe Pessoa com o nome "Maria" e idade 40.
# O construtor da classe Pessoa será chamado, e os atributos 'nome' e 'idade' da instância serão inicializados.
pessoa = Pessoa("Maria", 40)

# Cria um objeto da classe Estudante com o nome "João", idade 20, e matrícula "12345".
# O construtor da classe Estudante será chamado, inicializando os atributos 'nome', 'idade' e 'matricula'.
estudante = Estudante("João", 20, "12345")

# Cria um objeto da classe Professor com o nome "Carlos", idade 50, e disciplina "Matemática".
# O construtor da classe Professor será chamado, inicializando os atributos 'nome', 'idade' e 'disciplina'.
professor = Professor("Carlos", 50, "Matemática")

# Exibindo informações
pessoa.exibir_info()
estudante.exibir_info()  # Método herdado da classe Pessoa
estudante.estudar()  # Método específico da classe Estudante
professor.exibir_info()  # Método herdado da classe Pessoa
professor.ensinar()  # Método específico da classe Professor
