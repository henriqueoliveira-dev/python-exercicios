"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Produto:
  def __init__(self, nome, preco):

    self.nome = nome

    # self.preco = None # This line can be removed as set_preco will initialize _preco

    self.set_preco(preco)

  def get_preco(self):

    return self._preco

  def set_preco(self, preco):

    if preco >= 0:
        self._preco = preco # Corrected to set the internal price attribute
    else:
        print("Preco deve ser não-negativo")

  def aplicar_desconto(self, desconto_percentual):

    novo_preco = self._preco * (1 - desconto_percentual / 100)

    self.set_preco(novo_preco)

p1 = Produto("Camiseta", 50)

print(f"Preço atual de {p1.nome}: R$ {p1.get_preco()}")

p1.set_preco(60)

print(f"Novo preço de {p1.nome}: R$ {p1.get_preco()}")

p1.set_preco(-10)

p1.aplicar_desconto(10)

print(f"Preço após desconto de 10% de {p1.nome}: R$ {p1.get_preco()}")
#
