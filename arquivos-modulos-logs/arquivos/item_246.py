"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 63
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

with open('exercicio4.txt', 'w') as arquivo:
  for numero in range(0,101):
    if numero % 3 == 0:
       arquivo.write(str(numero) + '\n')
