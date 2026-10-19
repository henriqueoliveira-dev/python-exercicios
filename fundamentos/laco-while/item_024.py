"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 34
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

soma = 0

digito_zero = int(input("Digite um numero: "))

while digito_zero > 0:

    soma += digito_zero

    digito_zero = int(input("Digite outro numero: "))

print(f"A soma foi {soma}")
