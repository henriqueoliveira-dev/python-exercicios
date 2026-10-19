"""Conteúdo extraído de: 39_Lista_encadeada_simples.ipynb_1NDHQgrH.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
  
  def mostra_no(self):
    print(self.valor)
