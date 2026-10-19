"""Conteúdo extraído de: 19_Filas.ipynb_135wBpK3.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
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

# Importando a classe 'deque' do módulo 'collections'. 
# 'deque' é uma estrutura de dados de fila de dupla ponta, 
# mas neste exemplo, estamos usando apenas como uma fila simples.
from collections import deque

# Inicializando uma nova fila vazia.
fila = deque()

# Adicionando 'pessoa1' ao final da fila.
fila.append('pessoa1')

# Adicionando 'pessoa2' também ao final da fila. 
# Agora, 'pessoa1' é o primeiro da fila e 'pessoa2' é o segundo.
fila.append('pessoa2')

# Imprimindo a fila para visualização. 
# Neste ponto, a fila contém 'pessoa1' e 'pessoa2' em ordem.
print(fila)  # Saída: deque(['pessoa1', 'pessoa2'])

"""
First In, First Out (FIFO):

O conceito de "First In, First Out" (FIFO) rege as operações de uma 
fila. Isso significa que o primeiro elemento que foi adicionado à fila será o 
primeiro a ser removido.

Usando o exemplo da fila de pessoas novamente, se "pessoa1" se juntar à fila 
primeiro, seguida por "pessoa2" e depois "pessoa3", então "pessoa1" será a primeira 
a ser atendida e a sair da fila.

Aqui está como você pode implementar operações FIFO usando deque em Python:
"""

# Importando a classe 'deque' do módulo 'collections'. 
# 'deque' pode ser usado como uma fila de dupla ponta,

# mas neste exemplo, estamos usando apenas como uma fila simples.
from collections import deque

# Inicializando uma nova fila vazia.
fila = deque()

# Adicionando 'pessoa1' ao final da fila.
fila.append('pessoa1')  

# Adicionando 'pessoa2' ao final da fila.
fila.append('pessoa2')

# Adicionando 'pessoa3' ao final da fila.
fila.append('pessoa3')

# Imprimindo a fila para visualização. Neste ponto, a fila contém 
# 'pessoa1', 'pessoa2' e 'pessoa3' em ordem.
print(fila)  # Saída: deque(['pessoa1', 'pessoa2', 'pessoa3'])

# Removendo e retornando o elemento do início da fila, que neste caso é 'pessoa1'.
primeira_pessoa = fila.popleft()

# Imprimindo o nome da primeira pessoa, que foi removida da fila.
print(primeira_pessoa)  # Saída: 'pessoa1'

# Imprimindo a fila após a remoção de 'pessoa1'. 
# Agora a fila contém 'pessoa2' e 'pessoa3'.
print(fila)  # Saída: deque(['pessoa2', 'pessoa3'])

"""
As principais operações associadas às filas são enqueue (para adicionar 
um elemento ao final da fila) e dequeue (para remover o elemento do início). 
Em Python, usando deque, o método append pode ser usado para enqueue e o método 
popleft pode ser usado para dequeue.

Lembre-se de que, embora deque seja uma boa escolha para implementar filas, 
Python também oferece o módulo queue que fornece várias implementações de 
fila (como Simple Queue, Lifo Queue e PriorityQueue).
"""
print()
