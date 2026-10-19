"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 11
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  if num_lido >= 0:
    soma_atual += num_lido
  numeros_lidos += 1

media = soma_atual / 5
print("A soma dos números lidos é %.2f " % (soma_atual))
