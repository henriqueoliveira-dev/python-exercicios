"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 25
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")

else:
    print("Usuário ou senha incorretos.")
