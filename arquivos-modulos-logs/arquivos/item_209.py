"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

arquivo = open("exemplo.txt", "wt")
arquivo.write("Olá estou escrevendo no arquivo\n")
arquivo.write("Está é a sengunda linha do arquivo")
arquivo.close()
