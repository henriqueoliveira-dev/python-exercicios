"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 105
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

pessoas = []

for i in range(3):
    print("-" * 45)
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite sua cidade: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    pessoas.append(pessoa)

print("-" * 45)

for pessoa in pessoas:
    print(f"Nome: {pessoa["nome"]:<10}"
          f"Idade: {pessoa["idade"]:<5}"
          f"Cidade: {pessoa["cidade"]:<5}"

    )
