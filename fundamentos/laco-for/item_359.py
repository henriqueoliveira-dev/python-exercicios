"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

matriz_alunos = []

for i in range(3):

    nome = input(f"Digite o nome do aluno {i + 1}: ")

    notas = []

    for j in range(4):

        nota = float(input(f"Digite a nota {j + 1} do aluno {nome}: "))

        notas.append(nota)

    matriz_alunos.append([nome]+ notas)

for aluno in matriz_alunos:

    nome = aluno[0]

    notas = aluno[1:]

    media = sum(notas) / 4

    print("\n" + "-"*40)
    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media}")
