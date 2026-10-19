"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

matriz_pessoas = [
    [["Ana", 25], ["Bruno", 31], ["Carlos", 29], ["Alice", 34]],
    [["Amanda", 22], ["Beatriz", 45], ["Clara", 30], ["Arnaldo", 27]],
    [["Alfredo", 35], ["Bianca", 28], ["Cesar", 32], ["Ariel", 23]],
    [["Alberto", 40], ["Beto", 24], ["Camila", 21], ["Adriana", 37]]
]

for i in range(4):
    for j in range(4):
        nome = matriz_pessoas [i][j][0]
        idade = matriz_pessoas[i][j][1]
        if idade > 30:
           print(f" {nome} - {idade}")
