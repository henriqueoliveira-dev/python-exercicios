"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 95
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

numeros = [10,5, 6, 7, 8, 5, 7, 9, 5, 8, 5, 5]

contador = 0
for numero in numeros:
  if numero == 5:
    contador += 1

print(f"O número 5 aparece {contador} vezes.")
