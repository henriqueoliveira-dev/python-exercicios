"""Conteúdo extraído de: 27_Programa_o_Orientada_a_Objeto__POO_.ipynb_17d7kwHV.ipynb
Célula original: 50
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
3. Pilares da POO

    Polimorfismo: Permitindo que um objeto se comporte de diferentes maneiras.
        - Polimorfismo de sobrecarga.


O termo "polimorfismo" em programação orientada a objetos refere-se à
capacidade de objetos de classes diferentes serem tratados como objetos
de uma classe comum. No entanto, é importante notar que Python não suporta
polimorfismo de sobrecarga de métodos ou construtores como em algumas outras
linguagens de programação, como Java ou C++. Em Python, você não pode definir
múltiplos métodos com o mesmo nome que diferem apenas pelo número ou tipo de
seus parâmetros, o que é conhecido como "sobrecarga de métodos".

No entanto, podemos implementar um comportamento semelhante à sobrecarga em Python
usando argumentos padrão, argumentos variáveis ou condicionais dentro do método.

Vamos examinar um exemplo que demonstra como você poderia implementar um tipo de
"sobrecarga" em Python:

"""

"""

Exemplo: Classe Calculadora

Neste exemplo, vamos criar uma classe Calculadora que tem um método somar
que pode aceitar dois ou três números. Se receber dois números, ele retorna a
soma desses dois números. Se receber três, retorna a soma dos três.
"""

# Definindo uma classe chamada Calculadora.
class Calculadora:

    # Definindo um método chamado somar, que pode receber dois ou três números.
    # num3 é um argumento opcional com valor padrão None.
    def somar(self, num1, num2, num3=None):

        # Checando se o argumento num3 foi fornecido.
        if num3 is None:

            # Se num3 não foi fornecido (ou seja, é None), retornamos a
            # soma de num1 e num2.
            return num1 + num2

        else:

            # Se num3 foi fornecido, retornamos a soma de num1, num2 e num3.
            return num1 + num2 + num3


# Criando uma instância da classe Calculadora
calc = Calculadora()

# Utilizando o método somar com dois argumentos
print(calc.somar(5, 3))  # Saída: 8

# Utilizando o método somar com três argumentos
print(calc.somar(5, 3, 2))  # Saída: 10

"""
Neste exemplo, o método somar na classe Calculadora é capaz de aceitar
dois ou três números como argumentos, graças ao uso de um argumento padrão
para num3. Isso permite que você simule o comportamento da sobrecarga de métodos,
permitindo que o método somar opere de maneiras diferentes dependendo do número
de argumentos fornecidos.

Note que este não é um polimorfismo de sobrecarga no sentido estrito que você encontraria
em linguagens como Java ou C++. É apenas uma maneira de simular um comportamento semelhante em Python.
"""
print()
