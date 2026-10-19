"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício: Soma dos Números Pares em uma Matriz 4x4

Enunciado:

Dada a seguinte matriz 4x4:
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

    - Escreva um programa em Python que percorre cada elemento da matriz.
    - Some todos os números pares presentes na matriz.
    - Imprima o resultado da soma.

Dica: Use loops for aninhados para percorrer cada linha e coluna da matriz.
Utilize o operador % para verificar se um número é par.

Ao resolver o exercício, os alunos devem ser capazes de navegar pelos elementos
da matriz, aplicar condições lógicas e acumular valores baseados em critérios específicos.
"""

#Solução:

# Dada matriz 4x4
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Inicializa o acumulador para armazenar a soma dos elementos pares da matriz
soma_pares = 0

# Inicia um loop para percorrer as linhas da matriz
for linha in range(4):

    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(4):

        # Verifica se o elemento atual da matriz é par
        if M[linha][coluna] % 2 == 0:

            # Se o elemento for par, adiciona seu valor ao acumulador soma_pares
            soma_pares += M[linha][coluna]


# Imprimindo o resultado
print(f"A soma dos números pares da matriz é: {soma_pares}")
