"""Conteúdo extraído de: Banco_de_Exercícios_Python.ipynb
Célula original: 1
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
altura = float(input("Digite sua Altura: "))


cadastro_ativo = input("Cadsaro ativo? (Sim/Não): ")

if cadastro_ativo == "Sim":
   cadastro_ativo = True
   print(f"Cadatro ativo: {cadastro_ativo}")

   print(f"Tipo: {type(cadastro_ativo)}")

elif cadastro_ativo == "Não":
     cadastro_ativo = False
     print(f"Cadatro ativo: {cadastro_ativo}")

     print(f"Tipo: {type(cadastro_ativo)}")
