"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

#Somar uma coluna

#Podemos criar um código para somar os valores de uma coluna
#específica em uma matriz. Para este exemplo, vamos considerar
#que desejamos somar os valores da primeira coluna.

# Inicializa a matriz M com valores pré-definidos
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Imprime um título para a matriz
print("Matriz")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(4):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(4):

        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{M[linha][coluna]}", end="  ")

    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()

# Define a coluna que desejamos somar (neste caso, a primeira coluna, cujo índice é 0)
coluna_especifica = 0

# Inicializa o acumulador para armazenar a soma dos elementos da coluna especificada
soma_coluna = 0

# Inicia um loop para percorrer as linhas da matriz
for linha in range(4):

    # Adiciona o valor do elemento atual da coluna especificada ao acumulador soma_coluna
    soma_coluna += M[linha][coluna_especifica]

# Imprime a soma dos valores da coluna especificada
print(f"\nA soma dos valores da coluna {coluna_especifica} é: {soma_coluna}")


#Somar os valores da terceira linha:

# Define a linha que desejamos somar (neste caso, a terceira linha, cujo índice é 2)
linha_especifica = 2

# Inicializa o acumulador para armazenar a soma dos elementos da linha especificada
soma_linha = 0

# Inicia um loop para percorrer as colunas da matriz
for coluna in range(4):

    # Adiciona o valor do elemento atual da linha especificada ao acumulador soma_linha
    soma_linha += M[linha_especifica][coluna]

# Imprime a soma dos valores da linha especificada
print(f"A soma dos valores da linha {linha_especifica} é: {soma_linha}")
