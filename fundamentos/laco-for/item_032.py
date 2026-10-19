"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 49
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

numero = int(input("Digite um número: "))

maior = numero
menor = numero

for contador in range(2, 6):

    numero = int(input("Digite um número: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero
print("===================")
print(f"O número maior é {maior}.")
print(f"O número menor é {menor}.")
