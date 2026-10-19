"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 74
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

numeros = (5,6,790,89,36)

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(f"O maior valor é: {maior}")
