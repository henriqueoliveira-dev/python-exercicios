"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 20
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado.")

elif nota >= 5 and nota <= 6.9:
    print("Recuperação.")

elif nota < 5:
    print("Reprovado.")
