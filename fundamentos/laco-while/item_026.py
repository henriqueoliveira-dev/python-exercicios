"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 37
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Cadastrando...")

    elif opcao == 2:
        print("Consultando...")

    elif opcao == 3:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
