"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 51
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

quantidade = int(input("Quantos números você deseja informar? "))

soma = 0

for contador in range(quantidade):
    numero = int(input("Digite um número: "))
    soma += numero

media = soma / quantidade

print(f"A média é {media}")
