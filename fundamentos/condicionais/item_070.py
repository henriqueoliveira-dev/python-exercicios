"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 14
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("Classificação de idade.")
print("----------------------")
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
   print("Classificação: Criança")

elif idade >= 13 and idade <= 17:
     print("Classificação: Adolescente")

elif idade >= 18 and idade <= 59:
     print("Classificação: Adulto")

elif idade >= 60:
     print("Classificação: Idoso")
