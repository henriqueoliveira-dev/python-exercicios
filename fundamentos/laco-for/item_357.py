"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 5
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

#Somando coluna

M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(M)

print()

print("------ Matriz ------")
print()

for linha in range(4):

    for coluna in range(4):

        print(f"{M[linha][coluna]:4}", end="")
    print()

#Modeulo, somando coluna + linha:

coluna_especifica =2

soma_coluna = 0

for linha in range(4):

    soma_coluna += M[linha][coluna_especifica]

print(f"\nA soma dos valores da coluna {coluna_especifica} é: {soma_coluna}")

#Somando Linhas

linha_especificada = 2

soma_linha = 1

for coluna in range(4):

    soma_linha += M[linha_especificada][coluna]

print(f"\nA soma dos valores da linha {linha_especificada} é: {soma_linha}")
