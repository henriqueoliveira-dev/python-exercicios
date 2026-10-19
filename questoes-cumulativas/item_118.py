"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 115
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("------ Cadastro de Usuario -----")
print()
print("1 - Cadastrar")
print("2 - Listar")
print("3 - Pesquisar")
print("0 - Sair")

lista = []

while True:

    try:
        print('-' *32)
        opcao = int(input("Digite uma opção: "))

    except ValueError:
        print('-' *32)
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        print('-' *32)
        nome = input("Cadastre usuário: ")
        lista.append(nome)

    elif opcao == 2:
        print('-' *32)
        print("Nomes de usuários cadastrados:")

        for nome in lista:
            print(nome)

    elif opcao == 3:
        print('-' *32)
        pesquisa = input("Digite o nome que deseja pesquisar: ")

        encontrado = False

        for nome in lista:
            if pesquisa == nome:
                print("Usuário encontrado.")
                encontrado = True
                break

        if not encontrado:
            print('-' *32)
            print("Usuário não encontrado.")

    elif opcao == 0:
        print('-' *32)
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
