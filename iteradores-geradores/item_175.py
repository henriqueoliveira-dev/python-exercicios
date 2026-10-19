"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 5
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class ColecaoNumros:
  def __init__(self, numero_max):
    self.max = numero_max
  def __iter__(self):
    self.numero_atual = 1
    return self

  def __next__(self):
    if self.numero_atual <= self.max:
      retorno = self.numero_atual
      self.numero_atual += 1
      return retorno
    else:
      raise StopIteration

colecao = ColecaoNumros(6)
interador = iter(colecao)
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
print(next(interador))
#
