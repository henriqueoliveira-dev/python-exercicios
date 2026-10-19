"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Fruta:

    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):

        self.nome = nome
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque

manca = Fruta("Maçã", 2.5, 100)
banana = Fruta("Banana", 9.5, 90)
uva = Fruta("Uva", 18.5, 67)

def exibir_info(fruta):
    print(f"Nome da Fruta: {fruta.nome}")
    print(f"Preço por Kg: R${fruta.preco_por_kg:.2f}")
    print(f"Quantidade em Estoque: {fruta.quantidade_em_estoque}")

exibir_info(manca)
print("<--------------------------")
exibir_info(banana)
print("-------------------------->")
exibir_info(uva)
