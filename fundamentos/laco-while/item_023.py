"""Conteúdo extraído de: Exercicios-Simples.ipynb
Célula original: 32
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

senha_correta = "1234"

senha = input("Digite a senha: ")

while senha != senha_correta:

    print("Senha incorreta!")

    senha = input("Digite a senha novamente: ")

print("Acesso permitido!")
