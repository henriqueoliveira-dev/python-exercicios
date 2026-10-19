"""Conteúdo extraído de: Sistema de Cadastro de Clientes.ipynb
Célula original: 1
Origem registrada no manifesto: ZIP
Tipo: 🚀 Projeto/protótipo
"""

clientes = []

opcao = -1

while opcao != 0:

    print("=================================")
    print("      SISTEMA DE CLIENTES")
    print("=================================")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Pesquisar cliente")
    print("4 - Atualizar cliente")
    print("5 - Excluir cliente")
    print("6 - Relatório")
    print("0 - Sair")
    print("=================================")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:

        print("\n")
        print("====== CADASTRO DE CLIENTE ======")

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o CPF: ")
        telefone = input("Digite o telefone: ")
        renda = float(input("Digite a renda: "))

        cliente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone,
        "renda": renda
         }

        clientes.append(cliente)

    elif opcao == 2:
         print("\n")
         print("====== LISTAS DOS CLIENTES ======")

         print("-----------------------------")

         for cliente in clientes:
             print("Nome: ", cliente["nome"])
             print("Idade:", cliente["idade"])
             print("CPF:", cliente["cpf"])
             print("Telefone:", cliente["telefone"])
             print("Renda:", cliente["renda"])
             print("-----------------------------")

    elif opcao == 3:

         print("\n")
         print("====== PESQUISAR CLIENTE ======")

         busca = input("Digite o nome do cliente: ")

         for cliente in clientes:
            print("")
            print("---- Cliente encontrado! ----")
            print("Nome:", cliente["nome"])
            print("Idade:", cliente["idade"])
            print("CPF:", cliente["cpf"])
            print("Telefone:", cliente["telefone"])
            print("Renda:", cliente["renda"])
            print("-----------------------------")

    elif opcao == 4:
         print("\n")
         print("====== ATUALIZANDO CLIENTE ======")

         alterar = input("Digite o nome do cliente, que deseja altera:")

         for cliente in clientes:

             if cliente["nome"] == alterar:

              novo_nome = input("Digite um novo nome: ")
              cliente["nome"] = novo_nome
              print("Nome:", cliente["nome"])

              novo_idade = int(input("Digite uma nova idade: "))
              cliente["idade"] = novo_idade
              print("Idade:", cliente["idade"])

              novo_cpf = input("Digite um novo CPF: ")
              cliente["cpf"] = novo_cpf
              print("CPF:", cliente["cpf"])

              novo_telefone = input("Digite o novo telefone: ")
              cliente["telefone"] = novo_telefone
              print("Telefone:", cliente["telefone"])

              novo_renda = float(input("Digite uma nova renda: "))
              cliente["renda"] = novo_renda
              print("Renda:", cliente["renda"])

              print("-----------------------------")
              print("Cliente atualizado com sucesso!")

    elif opcao == 5:

         print("\n")
         print("====== EXCLUIR CLIENTE ======")

         nome_excluir = input("Digite o nome do cliente, que deseja excluir: ")

         for cliente in clientes:

             if cliente["nome"] == nome_excluir:

                clientes.remove(cliente)

                print("Cliente excluído com sucesso!")

             else:
                print("Cliente não encontrado!")

    elif opcao == 6:

         print("\n")
         print("====== RELATÓRIO CLIENTE ======")

         rendas = []]

         total_clientes = len(clientes)
         print(f"Total de clientes: {total_clientes}")

         for cliente in clientes:

            rendas.append(cliente["renda"])

            total_renda = sum(rendas)
            print(f"Soma das rendas: {total_renda}")

            media_renda = total_renda / total_clientes
            print(f"Média das rendas: {media_renda}")
