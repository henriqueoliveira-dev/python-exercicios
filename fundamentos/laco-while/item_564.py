"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 16
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

num_atual = 2
contador = 0

while (num_atual <= 10):
  resto = (num_atual % 2)
  if (resto == 0):
    print(num_atual, "é par")
  else:
    print(num_atual, "é ímpar")
  num_atual += 1
  contador += 1

print("A quantidade de números lidos foram: ", contador)
