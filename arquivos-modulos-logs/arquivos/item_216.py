"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

from os import path
arquivo_existe = path.exists("exemplo.txt")

if arquivo_existe == True:
   print("Arquivo existe")
else:
   print("Arquivo não existe")
