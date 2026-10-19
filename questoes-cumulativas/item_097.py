"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 72
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

dias_semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
               "Sexta-feira", "Sábado", "Domingo")

"""
① enumerate(dias_semana, start=1)
Essa função percorre a tupla dias_semana e fornece dois valores a cada repetição:
- O número da posição.
- O elemento que está naquela posição.
O start=1 determina que a numeração comece em 1.


② for numero, dia in ...
Aqui você cria duas variáveis para receber esses valores:
- numero recebe a numeração.
- dia recebe o nome do dia da semana.


③ print(f"Dia da semana {numero}: {dia}")
O print() exibe os dois valores. O f permite inserir as variáveis no texto usando {}.

"""

for numero, dia in enumerate(dias_semana, start=1):
    print(f"Dia da semana {numero}: {dia}")
