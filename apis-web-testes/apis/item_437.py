"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

"""
Exercício: Sistema de Reservas para um Evento

Objetivo: Compreender a definição e utilização de métodos dentro de classes em Python.

Descrição:

Crie uma classe chamada Evento que represente um evento com um número limitado de
lugares. A classe deve permitir:

    1. Reservar um lugar.
    2. Cancelar uma reserva.

A classe Evento deve ter os seguintes métodos:

    - reservar(): Este método deve diminuir o número de lugares disponíveis em um.
    - cancelar(): Este método deve aumentar o número de lugares disponíveis em um.
    - lugares_disponiveis(): Este método deve retornar o número de lugares disponíveis.

Restrições:

    1. O evento tem uma capacidade inicial definida (por exemplo, 10 lugares).

    2. Se tentar reservar um lugar e todos estiverem ocupados, o sistema deve
    informar que não há lugares disponíveis.

    3. Se tentar cancelar uma reserva e todos os lugares estiverem disponíveis,
    o sistema deve informar que não há reservas para cancelar.

"""
