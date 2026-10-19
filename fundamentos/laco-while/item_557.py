"""Conteúdo extraído de: 34_Estrutura_de_Programa_o-_WHILE.ipynb_1p1gag60.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

soma = 0
numeros_lidos = 0
contador = 0

while(numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma += num_lido
  numeros_lidos += 1
  contador += 1

print("A soma dos números lidos é: ", soma)
print("A quantidade de numeros somado foram: ", contador)
