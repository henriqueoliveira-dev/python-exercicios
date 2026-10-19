"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 29
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import csv
linhas = [
          ["id", "nome", "profisoão"],
          ["1", "Fernando", "Eng.de Dados"],
          ["2", "Maria", "Professora"],
]
with open('pessoas2.csv', 'w') as arquivo:

  escritorCsv = csv.writer(arquivo,delimiter=',')
  escritorCsv.writerows(linhas)
