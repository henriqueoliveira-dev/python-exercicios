"""Conteúdo extraído de: 35_Untitled0.ipynb_1HjI5KQQ.ipynb
Célula original: 16
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

senha = "123"
cpf = "12345678900"
senha_usuario = input("Digite sua senha: ")
cpf_usuario = input("Digite seu cpf: ")

if senha_usuario == senha and cpf_usuario == cpf:
  print("Acesso permitido, seu CPF é %s " % (cpf))
else:
  print("Acesso negado")
#
