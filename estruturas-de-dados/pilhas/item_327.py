"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

"""
 Filas

            Conceitos Básicos

                Definição e Estrutura: Compreender o que é uma fila e como ela é organizada.
                First In, First Out (FIFO): Entender o princípio básico que rege as operações de uma fila.


Filas (Queues)

Uma fila é outra estrutura de dados linear, mas, diferentemente das pilhas, os
elementos em uma fila são processados na ordem em que são adicionados. O lugar onde
os novos elementos são adicionados é chamado de "final" (ou "rear"), e o lugar de
onde os elementos são removidos é chamado de "início" (ou "front").

Imagine uma fila de pessoas esperando para comprar ingressos para um show. A primeira
pessoa que chega à fila será a primeira a comprar o ingresso e, consequentemente, a
primeira a sair da fila.

Em Python, as filas podem ser implementadas de várias maneiras, incluindo listas e o
módulo collections.deque. No entanto, usar listas para filas pode não ser eficiente,
especialmente para operações no início da lista, portanto, deque é frequentemente
preferido.
"""
