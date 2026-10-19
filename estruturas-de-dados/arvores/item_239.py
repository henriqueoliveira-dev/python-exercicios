"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 49
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import xml.etree.ElementTree as xml
import os

class Carro:
  def __init__(self, nome, potecia):
    self.nome = nome
    self.potecia = potecia

  @staticmethod
  def salva_carros(*carros):
    raiz = xml.Element("Raiz")

    for carro in carros:
      # Criamos o elemento Carro como filho direto de raiz
      no_carro = xml.SubElement(raiz, 'Carro')
      no_nome = xml.SubElement(no_carro, 'Nome')
      no_nome.text = carro.nome

      no_potencia = xml.SubElement(no_carro, 'Potencia')
      no_potencia.text = str(carro.potecia)

    arvore = xml.ElementTree(raiz)
    with open('carros_exemplo.xml', 'wb') as files:
      arvore.write(files)

  @staticmethod
  def le_carros():
    lista = []
    tree = xml.parse('carros_exemplo.xml')
    root = tree.getroot()
    for carro in root:
      nome = None
      potecia = None

      for dado in carro:
        if (dado.tag == 'Nome'):
          nome = dado.text
        elif (dado.tag == 'Potencia'):
          potecia = dado.text

      carro_obj = Carro(nome, potecia)
      lista.append(carro_obj)
    return lista

carro1 = Carro('Fusca', 40)
carro2 = Carro('Nivus', 450)
carro3 = Carro('Focus', 290)

Carro.salva_carros(carro1, carro2, carro3)

lista = Carro.le_carros()

for carro in lista:
  print(carro.nome, carro.potecia)
