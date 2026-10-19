"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

animais = [
    ["Gato", "Cachorro"],
    ["Pássaro", "Peixe"]
]

print(animais)

for i in range(2):
    for j in range(2):
        print(animais[i][j], end="  ")
    print()
