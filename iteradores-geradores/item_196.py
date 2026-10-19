"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 36
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Fatorial:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __iter__(self):
    self.atual = self.x -1
    return self

  @staticmethod
  def clacula_fatorial(num):
    result = 1
    for i in range(1,num+1):
      result *= i
    return result

  def __next__(self):
    self.atual += 1
    if(self.atual == self.y):
      raise StopIteration
    return self.clacula_fatorial(self.atual)

fatorial = Fatorial(1,10)
for i in fatorial:
  print(i)
#
