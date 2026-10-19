"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 34
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Tabada:
  def __init__(self,num):
    self.num = num
  def __iter__(self):
    self.atual = 0
    return self
  def __next__(self):
    self.atual += 1
    if(self.atual ==11):
      raise StopIteration
    return self.atual * self.num

tabuada_cal = Tabada(5)
for i in tabuada_cal:
  print(i)
#
