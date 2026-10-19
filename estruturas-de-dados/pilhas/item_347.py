"""Conteúdo extraído de: 21_Pilhas01.ipynb_19Pt4-ac.ipynb
Célula original: 2
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

class PilhaDeLivros:

    def __init__(self):

        self._livros = []

    def adicionar_livro(self, livro):

       self._livros.append(livro)

    def remover_livro(self):

        if not self.esta_vazia():

           return self._livros.pop()

        else:

            return None

    def ver_topo(self):

        if not self.esta_vazia():

           return self._livros[-1]

        else:

            return None
    def esta_vazia(self):

        return len(self._livros) == 0

    def quantidade(self):

        return len(self._livros)

pilha = PilhaDeLivros()

pilha.adicionar_livro("Livro A")
pilha.adicionar_livro("Livro B")
pilha.adicionar_livro("Livro C")
pilha.adicionar_livro("Livro D")
pilha.adicionar_livro("Livro E")

livros_guardador = []

for _ in range(3):
    livro_guardado = pilha.remover_livro()
    livros_guardador.append(livro_guardado)

print("Livros guardados:", livros_guardador)

pilha.adicionar_livro("Livro F")
pilha.adicionar_livro("Livro G")

livros_guardador2 = []

for _ in range(2):
    livro = pilha.remover_livro()
    livros_guardador2.append(livro)

print("O segundo bibliotecario guardou:", livros_guardador2)
