"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 47
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

positivos = 0
negativos = 0

for contador in range(1, 6):
    numero = int(input("Digite um número: "))

    if numero < 0:
        negativos += 1
    else:
        positivos += 1

print(f"Você digitou {negativos} números negativos.")
print(f"Você digitou {positivos} números positivos.")
