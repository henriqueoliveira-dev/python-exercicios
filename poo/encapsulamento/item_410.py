"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 24
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    - Encapsulamento: Protegendo os dados de uma classe.
        Uso de modificadores de acesso (public, private, protected).


"""

"""
A Programação Orientada a Objetos utiliza vários princípios, sendo um deles
o encapsulamento. O encapsulamento permite que os detalhes de implementação de
uma classe sejam ocultados, expondo apenas uma interface bem definida. Isso
é conseguido usando modificadores de acesso: public, private e protected.

    Public: Em Python, todos os membros de uma classe são públicos por
        padrão. Qualquer membro pode ser acessado de fora da classe.

    Protected: Um membro é considerado protegido se seu nome começa com
        um sublinhado único (_). Isso é mais uma convenção e um aviso para o
        programador de que o membro não deve ser acessado diretamente, embora
        ainda seja possível fazê-lo.

    Private: Um membro é considerado privado se seu nome começa com dois
        sublinhados (__). Novamente, isso é mais uma convenção do que uma regra
        rigorosa. O Python realiza um nome mangling dos atributos, alterando o nome
        do atributo de forma que ele seja mais difícil de ser acessado acidentalmente,
        mas ainda é possível.
"""

#Exemplo em Python

#Aqui está um exemplo de como usar esses modificadores
#de acesso em Python:

# Definindo a classe Pessoa
# Define uma classe chamada 'Pessoa'.
class Pessoa:

    # Define o método construtor '__init__' para inicializar os atributos da classe.
    def __init__(self, nome, idade):

        # Inicializa o atributo 'nome' da instância com o valor fornecido como argumento.
        # Este é um atributo público, significando que pode ser acessado diretamente de fora da classe.
        self.nome = nome

        # Inicializa o atributo '_idade' da instância com o valor fornecido.
        # Este é um atributo protegido, indicado pelo prefixo de sublinhado simples.
        # Ele pode ser acessado dentro da classe e suas subclasses, mas o acesso direto de fora da classe não é recomendado.
        self._idade = idade

        # Inicializa o atributo '__saldo' da instância com o valor 0.
        # Este é um atributo privado, indicado pelo prefixo de dois sublinhados.
        # Ele só deve ser acessado dentro da classe.
        self.__saldo = 0

    # Define um método público chamado 'mostrar_nome'.
    def mostrar_nome(self):

        # Retorna o valor do atributo 'nome'.
        return self.nome

    # Define um método público chamado 'mostrar_idade'.
    def mostrar_idade(self):

        # Retorna o valor do atributo '_idade'.
        return self._idade


    # Define um método protegido chamado '_aumentar_idade'.
    def _aumentar_idade(self):

        # Incrementa o valor do atributo '_idade' em 1.
        self._idade += 1


    # Define um método privado chamado '__aumentar_saldo'.
    def __aumentar_saldo(self, quantidade):

        # Incrementa o valor do atributo '__saldo' pela quantidade fornecida.
        self.__saldo += quantidade


    # Define um método público chamado 'depositar'.
    def depositar(self, quantidade):

        # Chama o método privado '__aumentar_saldo' para modificar o atributo '__saldo'.
        self.__aumentar_saldo(quantidade)

        # Retorna o valor atualizado do atributo '__saldo'.
        return self.__saldo


# Criando uma instância da classe Pessoa e inicializando-a com o nome "Alice" e a idade 30.
# A variável 'p' agora aponta para esta instância.
p = Pessoa("Alice", 30)


# ---- Atributos ----

# Acessando o atributo público 'nome' diretamente.
# Isso é totalmente aceitável porque o atributo é público.
print(p.nome)  # Saída: Alice

# Acessando o atributo protegido '_idade' diretamente.
# Embora isso seja possível, não é recomendado porque o atributo é marcado como protegido.
print(p._idade)  # Saída: 30

# Tentando acessar o atributo privado '__saldo' diretamente.
# Isso não é recomendado e requer uma técnica chamada "name mangling" para ser acessado.
# É melhor usar um método público para acessar atributos privados.
print(p._Pessoa__saldo)  # Saída: 0

# ---- Métodos Públicos -----

print("\nMétodos Públicos\n")

# Utilizando o método público para mostrar o nome novamente.
# Isso é útil se você precisar acessar o nome várias vezes no seu código.
print(p.mostrar_nome())  # Saída: Alice
print(p.mostrar_nome())  # Saída: Alice

# Utilizando o método público para mostrar a idade novamente.
# Isso é útil se você precisar verificar a idade em diferentes partes do código.
print(p.mostrar_idade())  # Saída: 30

# Fazendo um segundo depósito na conta usando um método público.
# Isso é útil para aumentar o saldo em etapas.
print(p.depositar(50)) # Saída: 50
print(p.depositar(50)) # Saída: 100
print(p.depositar(50)) # Saída: 150

# ---- Métodos Protegidos -----

print("\nMétodos Protegidos\n")

# Para usar um método protegido, você normalmente não deveria fazê-lo fora da classe ou subclasses.
# No entanto, para fins de demonstração, mostraremos como isso seria feito.

# Utilizando o método protegido para aumentar a idade.
# Embora isso seja possível, não é a prática recomendada.
p._aumentar_idade()  # Aumenta a idade em 1
p._aumentar_idade()  # Aumenta a idade em 1
print(p.mostrar_idade())  # Saída: 32 (idade aumentada em 2)


# ---- Métodos Privados -----

print("\nMétodos Privados\n")

# Você realmente não deveria acessar métodos privados fora da classe.
# Mas para fins educacionais, mostrarei como isso é tecnicamente possível usando name mangling.

# Utilizando name mangling para acessar um método privado (NÃO RECOMENDADO!)
p._Pessoa__aumentar_saldo(50)  # Aumenta o saldo em 50
print(p.depositar(0))  # Saída: 200 (saldo anterior era 150, aumentou para 200)

"""
O termo "name mangling" (ou "alteração de nome", em tradução livre) é uma
técnica usada em algumas linguagens de programação, incluindo Python, para alterar
o nome de um identificador (como uma variável ou método) de modo a torná-lo menos
acessível ou discernível fora do escopo onde foi definido.

Em Python, os atributos e métodos privados são precedidos por dois sublinhados (__).
O interpretador Python altera o nome desses membros para incluir o nome da
classe que os contém. Isso torna mais difícil para o código externo acessar
esses membros acidentalmente.
"""

# ---- O que não fazer ----

# A seguir estão alguns exemplos de práticas que não são recomendadas:

# Alterar diretamente um atributo protegido de fora da classe.
# Isso quebra o encapsulamento e pode levar a erros.
p._idade = 40  # Não recomendado

# Tentar acessar diretamente um método privado de fora da classe.
# Isso não funcionará a menos que você use name mangling, e ainda assim não é recomendado.
# p.__aumentar_saldo(100)  # Isso dará um erro

"""
Neste exemplo, nome é público, _idade é protegido e __saldo é privado.
Temos métodos públicos para interagir com esses atributos, bem como métodos
protegidos e privados (_aumentar_idade e __aumentar_saldo, respectivamente).

Note que mesmo o atributo privado __saldo pode ser acessado fora da classe
usando "name mangling", como em p._Pessoa__saldo. No entanto, essa não é uma
prática recomendada.
"""
print()
