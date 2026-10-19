"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

A = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

print("\nImprimindo Matriz A")
print()
print("Matriz A")

for linha in range(3):

    for coluna in range(3):

      print(f"{A[linha][coluna]}", end="  ")
    print()


B = [[1,2,3], [4,5,6], [7,8,9]]

print("\nMatriz B")

for linha in range(3):

  for coluna in range(3):

    print(f"{B[linha][coluna]}", end="  ")
  print()

D =[[0,0,0], [0,0,0], [0,0,0]]

print("\nMatriz D")

for linha in range(3):

  for coluna in range(3):

    print(f"{D[linha][coluna]}", end="  ")
  print()

print("\nSubtração das matrizes A e B")

for linha in range(3):

  for coluna in range(3):

    D[linha][coluna] = A[linha][coluna] - B[linha][coluna]

for linha in D:

    print(linha)


print("\nSoma das matrizes A e B")

for linha in range(3):

  for coluna in range(3):

    D[linha][coluna] = A[linha][coluna] + B[linha][coluna]

for linha in D:

    print(linha)
    print()

soma_diagonal = 0

for i in range(3):

    soma_diagonal += B[i][i]

print(f"A soma dos elementos da diagonal da Matriz B é: {soma_diagonal}")
