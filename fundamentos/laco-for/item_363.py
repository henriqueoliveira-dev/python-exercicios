"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

nomes = [
    ["Ana", "Bruno", "Carlos", "Alice"],
    ["Amanda", "Beatriz", "Clara", "Arnaldo"],
    ["Alfredo", "Bianca", "Cesar", "Ariel"],
    ["Alberto", "Beto", "Camila", "Adriana"]
]

for i in range(4):
    for j in range(4):
        if nomes[i][j][0] == "C":
           print(nomes[i][j])
