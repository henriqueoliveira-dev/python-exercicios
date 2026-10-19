"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Uma matriz de strings é basicamente uma lista de listas em
que cada elemento interno é uma string. Vamos a um exemplo prático:

Vamos considerar uma matriz 2x2, onde cada elemento é uma string
representando um nome de animal:

    Coluna 0    Coluna 1
0   "Gato"     "Cachorro"
1   "Pássaro"  "Peixe"

"""

# Criar e imprimir essa matriz:

# Criando a matriz 2x2 de strings
animais = [
    ["Gato", "Cachorro"],
    ["Pássaro", "Peixe"]
]

print(animais)

# Imprimindo a matriz
for i in range(2): # i representa as linhas
    for j in range(2): # j representa as colunas
        print(animais[i][j], end=" ")
    print() # Adiciona uma nova linha após cada linha da matriz

#Este é um exemplo mais direto e simplificado de uma matriz de strings em Python.
print()

"""
Vamos criar uma matriz 4x4 com alguns nomes e, em seguida, imprimir
apenas os que começam com a letra "A".

    Primeiro, criamos a matriz:

    0          1         2        3
0   "Ana"      "Bruno"   "Carlos" "Alice"
1   "Amanda"   "Beatriz" "Clara"  "Arnaldo"
2   "Alfredo"  "Bianca"  "Cesar"  "Ariel"
3   "Alberto"  "Beto"    "Camila" "Adriana"

"""

# Criando a matriz 4x4
nomes = [
    ["Ana", "Bruno", "Carlos", "Alice"],
    ["Amanda", "Beatriz", "Clara", "Arnaldo"],
    ["Alfredo", "Bianca", "Cesar", "Ariel"],
    ["Alberto", "Beto", "Camila", "Adriana"]
]

# Procurando e imprimindo nomes que começam com a letra 'A'
for i in range(4): # i representa as linhas
    for j in range(4): # j representa as colunas
        if nomes[i][j][0] == "A": # Checando se o primeiro caractere é 'A'
            print(nomes[i][j])

# Esses são os nomes na matriz 4x4 que começam com a letra 'A'.
