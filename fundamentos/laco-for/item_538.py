"""Conteúdo extraído de: 32_Listas.ipynb_1taQNADp.ipynb
Célula original: 55
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

dias = []
for i in range(1,32):
  dias.append(i)

dia_nascido = int(input("Digite o dia em que você nasceu: "))
dias.remove(dia_nascido)
print(dias )
