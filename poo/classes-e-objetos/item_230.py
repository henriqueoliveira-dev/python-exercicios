"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 32
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import csv

class Pessoa:

  def __init__(self, id, nome, profissao):
    self.id = id
    self.nome = nome
    self.profissao = profissao

  @staticmethod
  def le_pessoas():
    pessoas = []
    with open('pessoas.csv', 'r') as arquivo:
      leitor = csv.reader(arquivo, delimiter=',')
      for linha in leitor:
        pessoa = Pessoa(linha[0], linha[1], linha[2])
        pessoas.append(pessoa)
    return pessoas

  @staticmethod
  def salva_pessoas(*pessoas):
    with open('pessoas.csv', 'w') as arquivo:
      escritorCsv = csv.writer(arquivo, delimiter=',')
      for pessoa in pessoas:
         escritorCsv.writerow([pessoa.id, pessoa.nome, pessoa.profissao])

pessoa1 = Pessoa("1", "Fernando", "Eng.de Dados")
pessoa2 = Pessoa("2", "Maria", "Professora")
pessoa3 = Pessoa("3", "Rodrigo", "Dev")
pessoa4 = Pessoa("4", "Irene", "Tec. Informática")
Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3, pessoa4)

for pessoa in Pessoa.le_pessoas():
  print(pessoa.id, pessoa.nome, pessoa.profissao)
