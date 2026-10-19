"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 18
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

texto = input("Digite um texto: ")
indice = 0
num_vazio = 0

while (indice < len(texto)):
  if (texto[indice] == " "):
    num_vazio += 1
  indice += 1

print("A quantidade de espaços em branco é: ", num_vazio)
