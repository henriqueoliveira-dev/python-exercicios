"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 19
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

numero1 = int(input("Insira um numero: "))
numero2 = int(input("Insira um numero: "))

if numero1 > numero2:
  print("O maior numero é %d." %(numero1))
elif numero2 > numero1:
  print("O numero maior é %d." %(numero2))
else:
  print("Os numeros são iguais!")
