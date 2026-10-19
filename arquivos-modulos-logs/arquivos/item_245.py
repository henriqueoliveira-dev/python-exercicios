"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 61
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

with open('exercicio3.txt', 'w') as arquivo:
  for numero in range(0,101):
    arquivo.write(str(numero) + '\n')
