"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Matrizes:

        Inicializando as duas matrizes e a matriz resultado
        Usando loops for aninhados para subtrair elementos correspondentes
"""

#Exemplo Prático: Subtração de Matrizes 3x3 em Python

#A subtração de matrizes, assim como a adição, é uma operação elemento
#a elemento. Para subtrair duas matrizes, elas devem ter as mesmas dimensões.
#O resultado é uma nova matriz com a mesma dimensão, onde cada elemento é a diferença
#dos elementos correspondentes das duas matrizes originais.

#Inicializando as duas matrizes e a matriz resultado:

# Inicializa a matriz A com valores pré-definidos
A = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(A)

# Imprime uma quebra de linha seguida de um título para a matriz A
print("\nImprimindo Matriz A")

# Imprime o título para a matriz A
print("Matriz A:\n")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):

        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{A[linha][coluna]}", end="  ")

    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()


# Inicializa a matriz B com valores pré-definidos
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Imprime uma quebra de linha seguida de um título para a matriz B
print("\nMatriz B:")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):

        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{B[linha][coluna]}", end="  ")

    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()


# Inicializa a matriz D com todos os elementos sendo zero
D = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Imprime o título para a matriz D
print("\nMatriz D:")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):

        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{D[linha][coluna]}", end="  ")

    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()


# Subtração das matrizes A e B

print("\nSubtração das matrizes A e B")
# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):

        # Subtrai o valor da matriz B do valor correspondente na matriz A e armazena o resultado na matriz D
        D[linha][coluna] = A[linha][coluna] - B[linha][coluna]

# Inicia um loop para percorrer cada linha da matriz D
for linha in D:

    # Imprime a linha atual da matriz D
    print(linha)


print("\nSoma das matrizes A e B:")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):

        # Soma o valor da matriz A com o valor correspondente na matriz B e armazena o resultado na matriz D
        D[linha][coluna] = A[linha][coluna] + B[linha][coluna]

        # Imprime o valor resultante da soma atual seguido de dois espaços, sem quebrar a linha
        print(f"{D[linha][coluna]}", end="  ")

    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()


# Inicializa a variável que armazenará a soma dos elementos da diagonal principal da matriz
soma_diagonal = 0

# Inicia um loop para percorrer os elementos da diagonal principal da matriz 3x3
for i in range(3):

    # Adiciona o valor do elemento atual da diagonal principal ao acumulador soma_diagonal
    #soma_diagonal = soma_diagonal + B[i][i]
    soma_diagonal += A[i][i]

# Imprime o resultado da soma dos elementos da diagonal principal
print(f"\nA soma dos elementos da diagonal da matriz A é: {soma_diagonal}")
