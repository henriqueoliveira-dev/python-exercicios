"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

arquivo = open("exemplo.txt", "rt")
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()
print(primeira_linha)
print(segunda_linha)
arquivo.close()
