"""Conteúdo extraído de: 18_Filas01ipynb_1S2aJtUy.ipynb
Célula original: 9
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import queue
import threading
import time

fila = queue.Queue(maxsize=5)


def produtor():

    for i in range(10):

        print(f"Produzindo item {i}")

        fila.put(i)

        time.sleep(1)


def consumidor():

    for i in range(10):

        item = fila.get()

        print(f"Consumindo item {item}")

        time.sleep(1)


thread_produtor = threading.Thread(target=produtor)
thread_consumidor = threading.Thread(target=consumidor)


thread_produtor.start()
thread_consumidor.start()


thread_produtor.join()
thread_consumidor.join()


print("Fim!")
