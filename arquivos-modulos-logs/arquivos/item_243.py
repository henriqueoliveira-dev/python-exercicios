"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 57
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

Lista = []
with open('exercicio1.txt', 'r') as arquivo:
  for linha in arquivo:
    Lista.append(linha.strip())

print(Lista)
#
