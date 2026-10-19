"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 23
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import datetime

nome = input("Digite o nome do cliente: ")

data_txt = input("Digite a data de nascimento no formato dd/mm/aaaa: ")

data = datetime.datetime.strptime(data_txt, "%d/%m/%Y")

hoje = datetime.datetime(2026, 9, 13)

idade = hoje.year - data.year

if (hoje.month, hoje.day) < (data.month, data.day):
    idade -= 1

print(nome)

print(f"Você tem {idade} anos.")

print(f"Data de nascimento: {data.strftime('%d/%m/%Y')}")
