"""Conteúdo extraído de: 21_Pilhas01.ipynb_19Pt4-ac.ipynb
Célula original: 1
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Exercício: Simulação de Livros em uma Biblioteca

Imagine uma mesa em uma biblioteca onde os estudantes colocam os
livros que já leram. A mesa foi projetada de forma que só pode conter
uma pilha de livros. Cada vez que um estudante lê um livro, ele o coloca
no topo da pilha. E cada vez que um bibliotecário precisa guardar um
livro de volta na estante, ele sempre pega o livro do topo da pilha.

Tarefas:

    1. Crie uma classe PilhaDeLivros:

        - A classe deve ter uma lista privada _livros
            que inicialmente está vazia.

        - Deve ter métodos para adicionar_livro,
                                remover_livro,
                                ver_topo,
                                esta_vazia e quantidade.

    2. Simule o seguinte cenário usando a classe PilhaDeLivros:

        a. Cinco estudantes leram, em sequência, os
            livros: "Livro A", "Livro B", "Livro C", "Livro D" e "Livro E".
            Eles colocam cada livro na pilha após a leitura.

        b. Um bibliotecário vem e precisa guardar três livros de volta na
            estante. Ele pega os livros do topo da pilha. Quais são os livros
            que ele guardou?

        c. Dois estudantes vêm e colocam os livros "Livro F" e "Livro G" na
            pilha, respectivamente.

        d. Outro bibliotecário vem e pega dois livros do topo para guardá-los. Quais
            são os livros?

    Perguntas para reflexão:

        - Qual foi o último livro lido pelos estudantes e qual foi o primeiro a
              ser guardado pelos bibliotecários?

        - Qual é o estado final da pilha após todas as ações?

        - Baseado nesse exercício, você pode explicar o conceito
              de Last In, First Out (LIFO)?

Objetivo:

Este exercício ajuda a entender o conceito fundamental do LIFO, onde
o último item adicionado à pilha é o primeiro a ser removido dela. Ao
simular o cenário com livros em uma biblioteca, podem visualizar e
compreender melhor a natureza da pilha e suas operações.
"""
