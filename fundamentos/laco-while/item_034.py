"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 53
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

while True:

    print("\n===== Banco =====")
    print("1 - Consultar Saldo ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Sair ")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Consultandor...")

    elif opcao == 2:
        print("Depositando...")

    elif opcao == 3:
        print("Sacando...")

    elif opcao == 4:
        print("Saindo...")

        break

    else:
        print("Opção inválida!")
