"""Conteúdo extraído de: 🏥 Sistema de Atendimento de Pacientes.ipynb
Célula original: 0
Origem registrada no manifesto: ZIP
Tipo: 🚀 Projeto/protótipo
"""

from datetime import datetime
from zoneinfo import ZoneInfo


contador_preferencial = 0
contador_normal = 0


for paciente in range(5):

    print("========================================")
    print("  SISTEMA DE ATENDIMENTO DE PACIENTES   ")
    print("========================================")
    print()
    print("Bem-vindo!")
    print()
    print("Para iniciar o atendimento, informe seus")
    print("dados.")
    print("O sistema realizará automaticamente a")
    print("classificação e definirá sua prioridade")
    print("de atendimento.")
    print("----------------------------------------")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    # Estrutura_classificacao
    print()

    if idade >= 0 and idade <= 12:
        classificacao = "Amarelo"

    elif idade >= 13 and idade <= 59:
        classificacao = "Verde"

    elif idade >= 60:
        classificacao = "Vermelho"

    else:
        print("idade inválida")

    print(f"Classificação de Risco: {classificacao}")

    # Estrutura_prioridade

    if classificacao == "Amarelo":
        prioridade = "Preferencial 2"

    elif classificacao == "Verde":
        prioridade = "Normal"

    elif classificacao == "Vermelho":
        prioridade = "Preferencial 1"

    print(f"Prioridade: {prioridade}")

    # Gerando_senhas

    if prioridade == "Preferencial 1":
        contador_preferencial += 1
        print(f"Senha: P{contador_preferencial:03}")

    elif prioridade == "Preferencial 2":
        contador_preferencial += 1
        print(f"Senha: P{contador_preferencial:03}")

    elif prioridade == "Normal":
        contador_normal += 1
        print(f"Senha: N{contador_normal:03}")

    # Definindo_data_hora

    data_hora = datetime.now(ZoneInfo("America/Sao_Paulo"))

    data_formatada = data_hora.strftime("%d/%m/%Y - %H:%M")

    print(f"Entrada: {data_formatada}")

    print("----------------------------------------")
