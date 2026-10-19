"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

file = open('teste', 'w')
try:
  file.write('Hello World')
finally:
  file.close()

#
