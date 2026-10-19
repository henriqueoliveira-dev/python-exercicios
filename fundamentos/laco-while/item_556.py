"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 3
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

indice = 10
print("Programa começou")
while (indice >= 2):
  resto = (indice % 2)
  if (resto == 0):
    print(indice, "é par")
  else:
    print(indice, "é ímpar")
  indice -= 1

print("Programa terminou")
