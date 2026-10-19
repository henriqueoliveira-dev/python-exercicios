"""Conteúdo extraído de: 33_Estrutura_de_Programma_ao-_FOR_.ipynb_1bHs91e0.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

for y in range(1, 11):
    for x in range(1, 4):
        print("%d X %d = %2d" % (x, y, x*y), end="     ")
    print()
