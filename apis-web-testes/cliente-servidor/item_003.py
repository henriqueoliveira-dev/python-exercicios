"""Conteúdo extraído de: Banco_de_Exercícios_Python.ipynb
Célula original: 5
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

cpu = 150.00
memoria = 100.00
disco = 80.00

total_mensal = cpu + memoria + disco
print(f"Total Mensal: {total_mensal}")


total_anual = total_mensal * 12
print(f"Total Anua: {total_anual}")

porcentagem = (cpu / total_mensal) * 100
print(f"Percentual, custo total: {porcentagem:.2f} %")
