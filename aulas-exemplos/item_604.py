"""Conteúdo extraído de: 36_1Fundamentos-2.ipynb_1NZc_BNa.ipynb
Célula original: 31
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

sinal_vermelho = True
carro_vindo_direita = True
carro_vindo_esquerda = True
pode_atravessar = sinal_vermelho and not carro_vindo_direita and not carro_vindo_esquerda
print("Pode atravessar a rua? ", pode_atravessar)
