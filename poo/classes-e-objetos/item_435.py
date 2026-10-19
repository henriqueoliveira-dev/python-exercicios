"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Termostato:

    def __init__(self, temperatura_atual=20):
        self.temperatura = temperatura_atual

    def aumentar_temperatura(self, valor):
        self.temperatura += valor
        print(f"Temperatura aumentada em: {valor}º. Nova temperatura: {self.temperatura}º")

    def diminuir_temperatura(self, valor):
        self.temperatura -= valor
        print(f"Temperatura diminuída em: {valor}º. Nova temperatura: {self.temperatura}º")

    def configurar_temperatura(self, valor):
        self.temperatura = valor
        print(f"Temperatura configurada para: {self.temperatura}º")

    def mostrar_temperatura(self):
        print(f"Temperatura atual: {self.temperatura}º")


meu_termostato = Termostato(5)

meu_termostato.aumentar_temperatura(5)

meu_termostato.diminuir_temperatura(10)

meu_termostato.configurar_temperatura(10)

meu_termostato.mostrar_temperatura()

meu_termostato.aumentar_temperatura(50)

meu_termostato.diminuir_temperatura(35)
