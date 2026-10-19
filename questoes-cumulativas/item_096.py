"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 70
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

a = [1, 2, 3, 4]

b = [3, 4, 5, 6]

conjunto_a = set(a)
conjunto_b = set(b)

uniao = conjunto_a.union(conjunto_b)
intersecao = conjunto_a.intersection(conjunto_b)
diferenca = conjunto_a.difference(conjunto_b)

print(f"Resultado da união de A e B: {uniao}")
print(f"Resultado da intersecão de A e B: {intersecao}")
print(f"Diferenca de A e B: {diferenca}")
