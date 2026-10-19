"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 18
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

maior = None

for i in range(3):
    numero = int(input("Digite um numero: "))

    if maior is None:
        maior = numero

    elif numero > maior:
        maior = numero

print(f"O maior numero é: {maior}")
