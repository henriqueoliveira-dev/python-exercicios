"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 28
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import csv
with open('pessoas.csv', 'w') as arquivo:
  escritorCsv = csv.writer(arquivo,delimiter=',')
  escritorCsv.writerow(["id", "nome", "profisoão"])
  escritorCsv.writerow(["1", "Fernando", "Eng.de Dados"])
  escritorCsv.writerow(["2", "Maria", "Professora"])
  escritorCsv.writerow(["3", "Rodrigo", "Dev"])
  escritorCsv.writerow(["4", "Irene", "Tec. Informática"])
