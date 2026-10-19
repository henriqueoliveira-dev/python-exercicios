"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

lista = [str(i) + '\n' for i in range(0,20)]
arquivo = open("numeros_3.txt", "wt")
arquivo.writelines(lista)
arquivo.close()
