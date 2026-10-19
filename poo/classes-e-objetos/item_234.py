"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 39
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import json

class Carro:
  def __init__(self, nome, potecia):
    self.nome = nome
    self.potecia = potecia

  @staticmethod
  def salva_carros(*carros):
    dicionario = dict()
    for carro in carros:
      dicionario[carro.nome] = carro.potecia

    texto = json.dumps(dicionario, indent=4, ensure_ascii=False)
    with open('carros.json', 'w') as arquivo:
      arquivo.write(texto)

  @staticmethod
  def le_carros():
    lista = []
    texto = None
    with open('carros.json', 'rt') as arquivo:
      texto = arquivo.read()
      dicionario = json.loads(texto)
      for chave in dicionario:
        carro = Carro(chave, dicionario[chave])
        lista.append(carro)
    return lista

carro1 = Carro('Fusca', 40)
carro2 = Carro('Nivus', 450)
carro3 = Carro('Focus', 290)

Carro.salva_carros(carro1, carro2, carro3)
lista = Carro.le_carros()

for carro in Carro.le_carros():
  print(carro.nome, carro.potecia)
