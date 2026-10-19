"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 119
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

print("------ Cadastro de Produto -----")
print()
print("1 - Cadastrar Produtos")
print("2 - Listar Produtos")
print("3 - Atualizar Produtos")
print("4 - Pesquisar Produtos")
print("5 - Ecluir Produtos")
print("0 - Sair")


produtos = []

while True:
    try:
        print('-' *32)
        opcao = int(input("Digite uma opção: "))

    except ValueError:
        print('-' *32)
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço: ")
        quantidade = input("Digite a quantidade em estoque: ")

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)

    elif opcao == 2:
      print('-' *32)
      print("Produtos cadastrados no sistema :")

      for produto in produtos:
          print(produto)

    elif opcao == 0:
      print('-' *32)
      print("Saindo...")
      break
