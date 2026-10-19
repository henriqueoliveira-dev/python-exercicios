"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 111
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

nomes = []

while True:
  nome = input("Digite um nome: ")

  if nome == 'sair':
     break

  nomes.append(nome)

print(f'Lista com todos os nomes, listados: {nomes}')
