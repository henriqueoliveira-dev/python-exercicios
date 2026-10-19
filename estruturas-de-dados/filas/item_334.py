"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

"""
Exercício: Implementação de Fila de Prioridades

Objetivo: Implementar uma fila de prioridades em que
os elementos são removidos com base em uma chave de prioridade.

Contexto: Em muitos sistemas, algumas tarefas ou ações têm prioridades
diferentes. Por exemplo, em um sistema de atendimento ao cliente, certos
tickets podem ter prioridade alta devido à urgência do problema, enquanto
outros podem ser de baixa prioridade. Uma fila de prioridades pode ajudar a
gerenciar essas tarefas efetivamente.

Instruções:

    1. Implemente uma classe chamada FilaDePrioridades.
    2. A classe deve ter as seguintes operações:

        - enqueue(prioridade, elemento): Adicione um elemento à fila de
            prioridades. O parâmetro prioridade é um número (pode ser inteiro
            ou flutuante) que define a prioridade do elemento. O parâmetro elemento
            é o dado a ser armazenado na fila.

        - dequeue(): Remova e retorne o elemento com a mais alta
            prioridade (o menor valor de prioridade). Se a fila estiver
            vazia, retorne uma mensagem indicando isso.

        - peek(): Veja o elemento com a mais alta prioridade sem removê-lo.
            Se a fila estiver vazia, retorne uma mensagem indicando isso.

        - isEmpty(): Retorne True se a fila estiver vazia e False caso
            contrário.

        - getSize(): Retorne o número de elementos na fila.

    3. Depois de implementar a classe, crie uma instância da fila de prioridades
        e execute as seguintes ações:

        - Adicione três elementos à fila com diferentes prioridades.
        - Veja o elemento de mais alta prioridade sem removê-lo.
        - Remova o elemento de mais alta prioridade.
        - Veja o tamanho da fila.

"""
