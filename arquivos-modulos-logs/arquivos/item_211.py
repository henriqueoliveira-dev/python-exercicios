"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 3
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

lista = "Ana\nFernado\nJoão\nMaria"
arquivo = open("nome2.txt", "wt")
arquivo.write(lista)
arquivo.close()
