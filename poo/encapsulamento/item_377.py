"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Pessoa:

  def __init__(self, nome, idade):

    self.nome = nome

    self._idade = idade

    self.__saldo = 0

  def mostrar_nome(self):
      return self.nome  # Corrigido de self._nome para self.nome

  def _aumentar__idade(self):
      self._idade += 1

  def mostrar_idade(self):
      return self._idade # Adicionado o método para exibir a idade

  def _aumentar__saldo(self, quantidade):
      self.__saldo += quantidade

  def depositar(self, quantidade):

      self._aumentar__saldo(quantidade) # Corrigido o erro de digitação

  def mostrar_saldo(self):
      return self.__saldo

p = Pessoa("Alice", 30)

print(p.nome)
print(p._idade)

print(p._Pessoa__saldo)

#----- Métodos Publicos -----
print("\n")
print(p.mostrar_nome())

p.depositar(100)
p.depositar(100)
p.depositar(100)
p.depositar(-100)
print(p.mostrar_saldo())

#----- Métodos Protegidos -----

print("\n")
p._aumentar__idade()
print(p.mostrar_idade())
