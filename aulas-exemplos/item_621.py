"""Conteúdo extraído de: 36_1Fundamentos-2.ipynb_1NZc_BNa.ipynb
Célula original: 55
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

media_inputt = input("Digite a média do aluno: ")
nota_exame_input = input("Digite a nota do exame: ")
media = float(media_inputt)
nota_exame = float(nota_exame_input)
aprovado = (media >= 7) or (nota_exame >= 5)
print("O aluno foi aprovado? ", aprovado)
