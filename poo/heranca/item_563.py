"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

nuemros_que_devem_ser_lidos = float(input("Digite a quantidade de numeros que devem ser lidos: "))

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < nuemros_que_devem_ser_lidos):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma_atual += num_lido
  numeros_lidos += 1

media = soma_atual / 5
print("O total dos números lidos foram %.0f " % (soma_atual))
