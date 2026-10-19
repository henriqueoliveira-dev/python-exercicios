"""Conteúdo extraído de: 23_Matrizes_Aula01.ipynb_107ttUVd.ipynb
Célula original: 17
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

urna = [["Alice", 0], ["Bob", 0], ["Charlie", 0]]

for i in range(4):

    voto = input("Digite o nome do candidato (Alice, Bob ou Charlie): ")

    encontrado = False

    for candidato in urna:

        if candidato[0] == voto:

            candidato[1] += 1
            encontrado = True
            break

    if not encontrado:
        print("Voto nulo")


votos_maximos = -1
vencedor = ""
print("")
for candidato in urna:

    print(f"{candidato[0]}: {candidato[1]} votos")

    if candidato[1] > votos_maximos:

        votos_maximos = candidato[1]
        vencedor = candidato[0]


print(f"\nO vencedor é {vencedor} com {votos_maximos} votos!")
