"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 21
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

idade = int(input("Insira um idade: "))

if  (idade >= 0) and (idade <= 12):
  print("Classificação: \"Criança\".")

elif (idade >= 13) and (idade <= 17):
  print("Classificação: \"Adolescente\".")

elif (idade >=18) and (idade <= 59):
  print("Classificação: \"Adulto\".")

else:
  print("Classificação: \"Idoso\".")
