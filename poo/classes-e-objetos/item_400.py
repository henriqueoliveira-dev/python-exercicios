"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
2. Conceitos Básicos

    1. Classes e Objetos: Definindo e instanciando classes.
    2. Atributos: Definindo e acessando atributos de uma classe.
    3. Métodos: Definindo e chamando métodos de uma classe


    Classes e Objetos: Definindo e instanciando classes.

        Classe: É uma estrutura que define um tipo de dados, especificando as
        propriedades (atributos) e as ações (métodos) que um objeto desse tipo pode ter.
        Pense na classe como um blueprint ou um molde.

        Objeto: É uma instância da classe. Uma vez que você tem um molde (classe),
        você pode criar múltiplas cópias (objetos) desse molde. Cada objeto tem seu próprio
        conjunto de valores para os atributos definidos na classe.

        Esta declaração trata de criar o "molde" (classe) e depois fazer uma "cópia" desse
        molde (instanciar um objeto).

    Atributos: Definindo e acessando atributos de uma classe.

        Atributos: São as variáveis definidas dentro de uma classe. Eles mantêm o
        estado do objeto. Por exemplo, uma classe Carro pode ter atributos como cor,
        marca, velocidade_atual, etc.

        Esta declaração trata especificamente de como definir esses atributos em uma classe
        e, uma vez que um objeto é instanciado, como você pode acessar e possivelmente modificar
        esses atributos.

    Métodos: Definindo e chamando métodos de uma classe.

        Métodos: São funções definidas dentro de uma classe. Eles definem os comportamentos
        ou ações que um objeto dessa classe pode executar. Continuando com o exemplo da classe
        Carro, pode haver métodos como acelerar(), frear(), virar(), etc.

        Esta declaração é sobre como criar essas funções dentro de uma classe e como, após
        instanciar um objeto, você pode chamar esses métodos para executar ações ou
        comportamentos específicos.

Em resumo:

    O primeiro item é sobre a criação da estrutura geral e a materialização dessa
    estrutura em instâncias individuais.

    O segundo item foca nas propriedades que definem o estado de um objeto.

    O terceiro item é sobre as ações ou comportamentos que um objeto pode executar.

"""

# 1. Classes e Objetos

# Vamos criar uma classe Livro que representa um livro em nossa biblioteca.
# Definindo uma classe chamada Livro
class Livro:

    # O construtor da classe com três parâmetros: título, autor e ano

    """
        def:
            Esta é uma palavra-chave em Python usada para definir uma função.

    __init__:
        Este é um método especial ou um "método mágico" em Python. Ele é o construtor da
        classe. Sempre que você cria uma instância de uma classe (ou seja, um objeto da classe),
        este método é automaticamente chamado.

        A principal utilidade do método __init__ é inicializar os atributos do objeto recém-criado.

        (self, titulo, autor, ano): Estes são os parâmetros do método __init__.

        self: É uma referência ao objeto atual ou à instância da classe. Em
        Python, é uma convenção chamá-lo de "self", mas tecnicamente, você
        poderia dar a ele qualquer nome que quiser (embora isso possa ser confuso). Quando
        você cria uma instância de uma classe e chama um de seus métodos, Python
        automaticamente passa essa instância específica como o primeiro argumento para
        o método. Por isso, você precisa ter self como o primeiro parâmetro de todos os
        métodos de instância, para que eles possam acessar e modificar os atributos ou
        chamar outros métodos da mesma instância.

        titulo, autor, ano: São parâmetros adicionais que você passa quando cria uma
        instância da classe Livro. Eles são usados para inicializar os atributos correspondentes
        do objeto. No contexto do código fornecido, são usados para armazenar informações sobre
        o título, o autor e o ano de publicação de um livro.
    """
    def __init__(self, titulo, autor, ano):

        # Atribuindo o valor do parâmetro título à variável de instância titulo
        self.titulo = titulo

        # Atribuindo o valor do parâmetro autor à variável de instância autor
        self.autor = autor

        # Atribuindo o valor do parâmetro ano à variável de instância ano
        self.ano = ano

# Instanciando (criando) um objeto da classe Livro e passando os valores "1984", "George Orwell" e 1949 como argumentos
meu_livro = Livro("1984", "George Orwell", 1949)


#No código acima, Livro é uma classe que tem um construtor __init__.
#Usando a classe Livro, criamos um objeto meu_livro que representa o
#livro "1984" escrito por "George Orwell" e publicado em 1949.


#2. Atributos

#A classe Livro tem três atributos: titulo, autor e ano. Estes
# são definidos e inicializados no construtor __init__.

#Acessando os atributos do objeto meu_livro:

print(meu_livro.titulo)  # Saída: 1984
print(meu_livro.autor)   # Saída: George Orwell
print(meu_livro.ano)     # Saída: 1949

#3. Métodos

#Vamos adicionar um método à classe Livro que fornece uma
#descrição formatada do livro.

# Definindo uma classe chamada Livro: Esta classe será usada para
# criar objetos que representam livros.
class Livro:

    # O construtor da classe com três parâmetros: título, autor e ano
    # Este método é chamado automaticamente ao instanciar a classe.
    def __init__(self, titulo, autor, ano):

        # Atribuindo o valor do parâmetro 'titulo' à variável de instância 'titulo' do objeto.
        # Isso permite que cada objeto Livro tenha um título específico.
        self.titulo = titulo

        # Atribuindo o valor do parâmetro 'autor' à variável de instância 'autor' do objeto.
        # Isso permite que cada objeto Livro tenha um autor específico.
        self.autor = autor

        # Atribuindo o valor do parâmetro 'ano' à variável de instância 'ano' do objeto.
        # Isso permite que cada objeto Livro tenha um ano de publicação específico.
        self.ano = ano

    # Definindo um método chamado descricao: Este método retorna uma descrição formatada do livro.
    # Métodos são funções que pertencem a um objeto.
    def descricao(self):

        # Retornando uma string formatada que descreve o livro.
        # O método usa os atributos da instância (titulo, autor, ano) para criar essa descrição.
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano}"



# Instanciando e chamando o método
# Criando um novo objeto 'meu_livro' da classe Livro
# Nós passamos três argumentos: "1984" para o título, "George Orwell"
# para o autor e 1949 para o ano.
meu_livro = Livro("1984", "George Orwell", 1949)

# Chamando o método 'descricao' do objeto 'meu_livro'
# Isso irá executar o método 'descricao' definido na classe Livro e imprimir a
# descrição do livro.
print(meu_livro.descricao())  # Saída: '1984' por George Orwell, publicado em 1949


"""
No exemplo acima, adicionamos um método chamado descricao à
classe Livro. Este método retorna uma string formatada contendo
detalhes do livro. Depois de criar um objeto meu_livro, chamamos
esse método para obter e imprimir a descrição.

Com este exemplo prático, espero ter esclarecido os conceitos básicos
de classes, objetos, atributos e métodos na programação orientada a objetos em Python.
"""
print()
