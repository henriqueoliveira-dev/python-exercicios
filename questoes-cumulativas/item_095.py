"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 68
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

produtos = [
    "Mouse",
    "Teclado",
    "Mouse",
    "Monitor",
    "Teclado",
    "Headset",
    "Mouse",
    "Fone"
]

conjunto = set(produtos)

print(conjunto)

quantidade = len(conjunto)

print(f"Quantidade de produtos únicos: {quantidade}")
