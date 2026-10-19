"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

lista = ["Ana","Fernado","João", "Maria"]
arquivo = open("nome.txt", "wt")
for i in lista:
  arquivo.write(i+"\n")
arquivo.close()
#
