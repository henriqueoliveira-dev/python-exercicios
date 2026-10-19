"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício:

Dada a matriz matriz_pessoas, escreva um programa que imprima
os nomes das pessoas com mais de 30 anos.

    matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]
]

"""

# Solução:

# Criando uma matriz 4x4, onde cada elemento é uma lista contendo um nome e uma idade.
matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],  # Primeira linha da matriz
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],  # Segunda linha da matriz
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],  # Terceira linha da matriz
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]  # Quarta linha da matriz
]

# Iniciando um loop para percorrer cada linha da matriz
for i in range(4):

    # Iniciando um loop interno para percorrer cada coluna da matriz
    for j in range(4):

        # Extraindo o nome da pessoa na posição atual da matriz
        nome = matriz_pessoas[i][j][0]

        # Extraindo a idade da pessoa na posição atual da matriz
        idade = matriz_pessoas[i][j][1]

        # Verificando se a idade da pessoa é maior que 30
        if idade > 30:

            # Imprimindo o nome da pessoa caso a condição acima seja verdadeira
            print(f"{nome} - {idade}")
