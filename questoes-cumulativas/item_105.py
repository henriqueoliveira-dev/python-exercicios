"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 88
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

produtos_ecommerce = [
    {"nome": "Teclado", "preco": 108.90, "estoque": 50},
    {"nome": "Monitor", "preco": 189.89, "estoque": 100},
    {"nome": "Mouse", "preco": 25.99, "estoque": 200},
    {"nome": "Impressora", "preco": 399.00, "estoque": 700},
    {"nome": "Memoria Ram - 16gb", "preco": 899.89, "estoque": 900}
]


for produto in produtos_ecommerce:
    print(
        f"{produto['nome']:<25}"
        f"R$ {produto['preco']:>6.2f}"
        f"{produto['estoque']:>10} unidades"
    )
