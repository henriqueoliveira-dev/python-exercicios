"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 97
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

nomes = ["Henrique", "Ana", "Carlos", "João", "Mariana", "Lucas"]

contador = 0

for nome in nomes:
  if len(nome) > 5:
    contador += 1

print(f"Existem {contador} nomes com mais de 5 caracteres.")
