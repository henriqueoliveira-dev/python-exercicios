"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 28
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
Exercício Pet

Instruções do Exercício

    1. Crie uma classe chamada Pet.
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos.

        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.

    3. Adicione um método exibir_info() que mostre as informações do pet.


# Teste sua implementação
meu_pet = Pet()
meu_pet.set_nome("Buddy")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

Sua tarefa é completar a classe Pet seguindo as instruções.
Certifique-se de utilizar "getters" e "setters" para controlar o acesso aos
atributos da classe.
"""

#Solução

# 1. Crie uma classe chamada Pet.
# Definindo a classe Pet
class Pet:

    """
    2. A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.
        - Utilize métodos "getters" para cada um desses atributos.
        - Utilize métodos "setters" para cada um desses atributos.
    """
    # Método construtor para inicializar os atributos quando um objeto da classe é criado
    def __init__(self):

        # Inicializa o atributo '_nome' como uma string vazia.
        # O prefixo "_" indica que é um atributo protegido.
        self._nome = ""

        # Inicializa o atributo '_idade' como 0.
        # O prefixo "_" indica que é um atributo protegido.
        self._idade = 0

        # Inicializa o atributo '_peso' como 0.0.
        # O prefixo "_" indica que é um atributo protegido.
        self._peso = 0.0

    # Método "getter" para o nome, permite obter o valor do atributo '_nome'
    def get_nome(self):

        return self._nome

    """
    Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
            - O peso deve ser um número flutuante e deve ser maior que 0.
    """

    # Método "setter" para o nome, permite definir um novo valor para o atributo '_nome'
    def set_nome(self, novo_nome):

        """
        Os "setters" devem conter as seguintes validações:
            - O nome deve ser uma string e não pode ser vazio.
        """
        # Verifica se o novo_nome é uma string e se não está vazio
        if isinstance(novo_nome, str) and novo_nome != "":

            # Atualiza o valor do atributo '_nome'
            self._nome = novo_nome

        else:

            # Imprime uma mensagem de erro se o nome fornecido não for válido
            print("Nome inválido.")

    # Método "getter" para a idade, permite obter o valor do atributo '_idade'
    def get_idade(self):

        return self._idade


    # Método "setter" para a idade, permite definir um novo valor para o atributo '_idade'
    def set_idade(self, nova_idade):

        """
            Os "setters" devem conter as seguintes validações:
            - A idade deve ser um número inteiro e deve ser maior ou igual a 0.
        """
        # Verifica se a nova_idade é um inteiro e se é maior ou igual a 0
        if isinstance(nova_idade, int) and nova_idade >= 0:

            # Atualiza o valor do atributo '_idade'
            self._idade = nova_idade

        else:

            # Imprime uma mensagem de erro se a idade fornecida não for válida
            print("Idade inválida.")

    # ---------------------------------------------

    # Método "getter" para o peso, permite obter o valor do atributo '_peso'
    def get_peso(self):

        return self._peso

    # Método "setter" para o peso, permite definir um novo valor para o atributo '_peso'
    def set_peso(self, novo_peso):

        """
        Os "setters" devem conter as seguintes validações:
                - O peso deve ser um número flutuante e deve ser maior que 0.
        """

        # Verifica se o novo_peso é um número flutuante e se é maior que 0
        if isinstance(novo_peso, float) and novo_peso > 0:

            # Atualiza o valor do atributo '_peso'
            self._peso = novo_peso

        else:

            # Imprime uma mensagem de erro se o peso fornecido não for válido
            print("Peso inválido.")



    # 3. Adicione um método exibir_info() que mostre as informações do pet.
    def exibir_info(self):

        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} kg")


# Teste sua implementação
meu_pet = Pet()
meu_pet.set_nome("Bob")
meu_pet.set_idade(5)
meu_pet.set_peso(9.5)
meu_pet.exibir_info()

print("\n-----------------\n")

meu_pet.set_nome("Toto")
meu_pet.set_idade(8)
meu_pet.set_peso(7.5)
meu_pet.exibir_info()

print("\n-----------------\n")

meu_pet.set_nome("Lua")
meu_pet.set_idade(12)
meu_pet.set_peso(9.3)
meu_pet.exibir_info()
