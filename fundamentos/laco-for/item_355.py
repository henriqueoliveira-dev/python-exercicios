"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 3
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

#Solução:

M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma_pares = 0

for linha in range(4):

    for coluna in range(4):

        if M[linha][coluna] % 2 == 0:

            soma_pares += M[linha][coluna]

soma_impares =0

for linha in range(4):

    for coluna in range(4):

        if M[linha][coluna] % 2 != 0:

            soma_impares += M[linha][coluna]

soma_total =0

for linha in range(4):

    for coluna in range(4):

         if M[linha][coluna]:

             soma_total += M[linha][coluna]

#Quantidade Elementos
quant_elementos =0

quantidade = len(M) * len(M[0])

#Saidas

print(f"A soma dos números da matriz é: {soma_pares}")
print("")

print(f"A soma dos números da matriz é: {soma_impares}")
print("")

print(f"Soma de total de elementos dentro da Matriz: {soma_total}")

print("")
print(f"A quantidade de elementos dentro da Matriz é: {quantidade}")
