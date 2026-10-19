"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 109
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("==================================================")
print("|          CONTADOR, SOMA E MÉDIA                | ")
print("==================================================")

quantidade = 0
soma = 0
maior = None
menor = None

while True:
    numero = float(input("Digite sua nota: "))

    if numero == 0:
        break

    if maior is None:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    quantidade += 1

    soma += numero
    quantidade += 1

media = soma / quantidade



print("-" * 50)
print(f"Soma das notas: {soma}")
print("-" * 50)
print(f"Quantidade de notas: {quantidade}")
print("-" * 50)
print(f"Média das notas: {media:.2f}")
print("-" * 50)
print(f"Maior numero é : {maior}")
print("-" * 50)
print(f"Menor numero é: {menor}")
