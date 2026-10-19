"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 55
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

numero_secreto = 7

tentativa = 0

while tentativa != numero_secreto:

    tentativa = int(input("Digite um número: "))

    if tentativa > numero_secreto:
       print("Tente um numero menor!")

    elif tentativa < numero_secreto:
      print("Tente um numero maior!")
else:
  print("Parabéns! Você acertou!")
