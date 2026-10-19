"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 40
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

palavra = input("Digite uma palavra: ")

contador = 0

for i in palavra:
    if i == "a":
        contador += 1

print(f"A palavra possui {contador} 'a'.")
