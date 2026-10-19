"""Conteúdo extraído de: Banco_de_Exercícios_Python.ipynb
Célula original: 12
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("=" * 42)
print("|" + " " * 40 + "|")
print("|" + " CÁLCULO DE JUROS COMPOSTOS".center(40) + "|")
print("|" + " " * 40 + "|")
print("=" * 42)

print("""
Este programa calcula o montante final de
um investimento com base no capital inici-
ial, na taxa de juros mensal e no período
de aplicação.

Informe os dados abaixo para realizar o
cálculo:
""")

capital = float(input("Digite o capital inicial: R$ "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite o número de meses: "))

taxa = taxa / 100

montante = capital * (1 + taxa) ** meses

print("=" * 42)
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa mensal: {taxa * 100:.2f}%")
print(f"Período: {meses} meses")
print(f"Montante final: R$ {montante:.2f}")
print("=" * 42)
