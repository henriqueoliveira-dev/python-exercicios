"""Conteúdo extraído de: 37_1.Fundamentos.ipynb_1yzSVou-.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

nome = "Alice"
idade = 30

# Usando %s para strings
mensagem1 = "Olá, meu nome é %s." % nome
print(mensagem1)

# Usando %s para qualquer tipo de dado (ele será convertido para string)
mensagem2 = "Tenho %s anos." % idade
print(mensagem2)

# Usando múltiplos %s com uma tupla
mensagem3 = "Meu nome é %s e tenho %s anos." % (nome, idade)
print(mensagem3)
