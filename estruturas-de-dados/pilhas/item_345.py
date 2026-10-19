"""Conteúdo extraído de: 21_Pilhas01.ipynb_19Pt4-ac.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

class Pilha:

   def __init__(self):

       self.pratos = []

   def adicionar(self, prato):

       self.pratos.append(prato)

   def remover(self):

       if not self.esta_vazia():

          return self.pratos.pop()

   def esta_vazia(self):

      return len (self.pratos) == 0

   def ver_topo(self):

       if not self.esta_vazia():

          return self.pratos[-1]

       return None

   def quantidade(self):

       return len(self.pratos)


minha_pilha = Pilha()

minha_pilha.adicionar("Prato 1")
print("Adicionando o Prato 1")


minha_pilha.adicionar("Prato 2")
print("Adicionando o Prato 2")

minha_pilha.adicionar("Prato 3")
print("Adicionando o Prato 3")

print("Topo da pilha:", minha_pilha.ver_topo())

prato_removendo = minha_pilha.remover()

print("Removendo o Prato 3")

prato_removendo = minha_pilha.remover()

print("Removendo o Prato 2")

minha_pilha.adicionar("Prato 4")
print("Adicionando o Prato 4")

print("Topo da pilha:", minha_pilha.ver_topo())

print("Quantidade de pratos na pilha:", minha_pilha.quantidade())

if minha_pilha.esta_vazia():

   print("A pilha está vazia.")

else:

   print("A pilha não está vazia.")

num_pratos = minha_pilha.quantidade()

print("Quantidade de pratos na pilha:", num_pratos)
