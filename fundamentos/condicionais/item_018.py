"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 23
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("==== Calculadora ====")
print("")
print(" 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")
print("")
print("=====================")
numero_operacao = int(input("Escolha o numero de operação: "))

# Primeiro verificamos se o usuário quer sair
if numero_operacao == 0:
    print("Encerrando a calculadora...")

# Se não quiser sair, aí pedimos os números
elif numero_operacao >= 1 and numero_operacao <= 4:

    numero1 = float(input("Insira um numero: "))
    numero2 = float(input("Insira um numero: "))


    if numero_operacao == 1:
        resultado = numero1 + numero2
        print(f"Resultado: {resultado:.0f}")

    elif numero_operacao == 2:
        resultado = numero1 - numero2
        print(f"Resultado: {resultado:.0f}")

    elif numero_operacao == 3:
        resultado = numero1 * numero2
        print(f"Resultado: {resultado:.0f}")

    elif numero_operacao == 4:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado:.0f}")



else:
    print("Opção inválida!")
    exit()
