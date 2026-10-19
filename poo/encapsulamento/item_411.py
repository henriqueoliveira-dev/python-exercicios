"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 26
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    Encapsulamento: Protegendo os dados de uma classe.

        Métodos getters e setters.

Em programação orientada a objetos, os métodos "getters" e "setters"
são usados para controlar o acesso a atributos de uma classe.

Os "getters" são usados para acessar o valor de um atributo, enquanto
os "setters" são usados para modificar esse valor.

Essa abordagem é especialmente útil para adicionar uma camada extra de validação
ou lógica durante o acesso ou modificação de atributos.

Vamos considerar uma classe Produto que tem um preço. Queremos garantir
que o preço nunca seja negativo e que possamos aplicar um desconto ao
produto se necessário. Usaremos métodos "getters" e "setters" para controlar esses aspectos.

"""

# Definição da classe Produto
class Produto:

    # Método construtor para inicializar atributos da classe
    def __init__(self, nome, preco):

        # Atributo público 'nome' para armazenar o nome do produto
        # Público significa que esse atributo pode ser acessado diretamente de fora da classe
        self.nome = nome

        # Atributo protegido '_preco' para armazenar o preço do produto
        # Protegido significa que esse atributo deve ser acessado apenas dentro desta classe e suas subclasses
        # Inicializamos com None para indicar que ele ainda não tem um valor definido
        self._preco = None

        # Usamos o método setter set_preco() para inicializar o preço do produto
        # Isso garante que todas as regras de validação sejam aplicadas desde o início
        self.set_preco(preco)

    # Método getter para obter o preço atual do produto
    # Este método é usado para ler o valor do atributo protegido '_preco'
    def get_preco(self):

        return self._preco


    # Método setter para definir um novo preço para o produto
    # Este método é usado para modificar o valor do atributo protegido '_preco'
    def set_preco(self, valor):

        # Verificamos se o valor fornecido é um número não-negativo
        # Essa é uma regra de negócio que queremos impor
        if valor >= 0:
            self._preco = valor  # Se a verificação passar, atualizamos o valor de '_preco'
        else:
            print("Preço deve ser não-negativo")  # Se a verificação falhar, exibimos uma mensagem de erro

    # Método para aplicar um desconto percentual ao preço do produto
    # Este método modifica o atributo '_preco', aplicando um desconto a ele
    def aplicar_desconto(self, desconto_percentual):

        # Calculamos o novo preço após aplicar o desconto
        # O cálculo é feito tomando o preço original e subtraindo a porcentagem de desconto
        novo_preco = self._preco * (1 - desconto_percentual / 100)

        # Usamos o método setter set_preco() para atualizar o preço do produto com o novo valor
        # Isso garante que todas as regras de validação sejam novamente aplicadas
        self.set_preco(novo_preco)


# Criando um objeto Produto
p1 = Produto("Camiseta", 50)

# Obtendo o preço usando o método getter
print(f"Preço atual de {p1.nome}: R$ {p1.get_preco()}")  # Saída: Preço atual de Camiseta: R$ 50

# Definindo um novo preço usando o método setter
p1.set_preco(60)

print(f"Novo preço de {p1.nome}: R$ {p1.get_preco()}")  # Saída: Preço atual de Camiseta: R$ 60


# Tentando definir um preço negativo
p1.set_preco(-10)  # Saída: Preço deve ser não-negativo

# Aplicando um desconto de 10% ao produto
p1.aplicar_desconto(10)

print(f"Preço de {p1.nome} após desconto R$ {p1.get_preco()}")  # Saída: Preço de Camiseta após desconto: R$ 54.0
