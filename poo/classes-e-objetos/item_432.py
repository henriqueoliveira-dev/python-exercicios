"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Jogador:
    def __init__(self, nome, posicao, numero_camisa, gols=0):
        self.nome = nome
        self.posicao = posicao
        self.numero_camisa = numero_camisa
        self.gols = gols

    def marcar_gol(self):
        self.gols += 1

jogador1 = Jogador("Roberto", "Atacante", 9)
jogador2 = Jogador("Carlos", "Goleiro", 1)

print(f"{jogador1.nome} é um {jogador1.posicao} e usa camisa número {jogador1.numero_camisa}")
print(f"{jogador2.nome} é um {jogador2.posicao} e usa camisa número {jogador2.numero_camisa}")

jogador1.gols += 1
jogador1.gols += 1
jogador1.gols += 1

print(f"{jogador1.nome} fez {jogador1.gols} gol(s) até agora.")

jogador2.gols += 9

print(f"{jogador2.nome} fez {jogador2.gols} gol(s) até agora.")
#
