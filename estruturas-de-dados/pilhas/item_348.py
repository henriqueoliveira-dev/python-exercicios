"""Conteúdo extraído de: 22_Pilhas.ipynb_1PHPSsF8.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
Pilhas

        Conceitos Básicos

            Definição e Estrutura: Entender o que é uma pilha e como ela é organizada.


Pilhas: Pilhas são uma estrutura de dados linear que segue o princípio
de Last In First Out (LIFO). Isso significa que o último elemento inserido
na pilha será o primeiro a ser removido. As operações básicas associadas
às pilhas são: push (adicionar um item ao topo) e pop (remover o item do topo).


Definição e Estrutura:


1 - Definição:

Uma pilha é uma coleção ordenada de itens na qual a adição
de novos itens e a remoção de itens existentes sempre ocorrem no mesmo
final. Esse final é comumente referido como o "topo". O final oposto da
pilha é conhecido como "base".


2 - Características:

A pilha é uma estrutura LIFO (Last In, First Out).

Somente o elemento no topo da pilha é acessível. Para acessar
outros elementos, você teria que remover os que estão no topo primeiro.


3 - Operações Básicas:

push(): Adiciona um item ao topo da pilha.

pop(): Remove e retorna o item do topo da pilha.

peek() ou top(): Retorna o item do topo sem removê-lo.

is_empty(): Verifica se a pilha está vazia.

size(): Retorna o número de elementos na pilha.


Em Python, podemos implementar pilhas usando listas ou através da
classe deque da biblioteca collections
"""
print()
