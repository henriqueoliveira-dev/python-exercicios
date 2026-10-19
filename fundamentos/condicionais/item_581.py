"""Conteúdo extraído de: 35_Untitled0.ipynb_1HjI5KQQ.ipynb
Célula original: 20
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
opracao = input("Digite a operação (+, -, *, /): ")

if opracao == "+":
  resultado = numero1 + numero2
  print("O resultado é: %.0f" % (resultado))
elif opracao == "-":
  resultado = numero1 - numero2
  print("O resultado é: %.0f" % (resultado))
elif opracao == "*":
  resultado = numero1 * numero2
  print("O resultado é: %.0f" % (resultado))
elif opracao == "/":
  resultado = numero1 / numero2
  print("O resultado é: %.2f" % (resultado))
else:
  print("Operação inválida")
