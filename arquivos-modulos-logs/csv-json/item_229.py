"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 31
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import  csv
with open('pessoas.csv', 'r') as arquivo:
  leitorCsv = csv.reader(arquivo, delimiter=',')
  for linha in leitorCsv:
    print(linha)
