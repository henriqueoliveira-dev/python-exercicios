"""Conteúdo extraído de: 35_Untitled0.ipynb_1HjI5KQQ.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

nome = input("Digite seu nome: ")
possui_volgal = ("a" in nome) or ("e" in nome) or ("i" in nome) or ("o" in nome) or ("u" in nome)

if possui_volgal:
    print("Possui volgal")
else:
    print("Não possui volgal")
