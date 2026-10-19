"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 113
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("------ Cadastro de Usuario -----")
print()
print("1 - Cadastrar")
print("2 - Listar")
print("0 - Sair")

lista = []

while True:

    try:
        opcao = int(input("Digite uma opção: "))

    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        nome = input("Cadastre usuário: ")
        lista.append(nome)

    elif opcao == 2:
        print(f"Nomes de usuários cadastrados: {lista}")

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
