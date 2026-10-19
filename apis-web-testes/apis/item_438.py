"""Conteúdo extraído de: 28_7.Orienta_oObjetos.ipynb_13SIpRWo.ipynb
Célula original: 13
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

class Evento:

  def __init__(self, capacidade=10):

    self.capacidade = capacidade
    self.lugares_disponiveis = capacidade

  def reservar(self):

      if self.lugares_disponiveis == 0:

         print("Desculpe, não há lugares disponíveis para reservar.")

         return

      self.lugares_disponiveis -= 1

      print("Lugar reservado com sucesso!")

  def mostrar_lugares_disponiveis(self):

         return f"Lugares Disponíveis: {self.lugares_disponiveis}"

  def cancelar(self):

      if self.lugares_disponiveis == self.capacidade:

         print("Não há reservas para cancelar.")

         return

      self.lugares_disponiveis += 1

      print("Reserva cancelada com sucesso!")

evento = Evento()

print(evento.mostrar_lugares_disponiveis())
evento.reservar()
print(evento.mostrar_lugares_disponiveis())
evento.reservar()
print(evento.mostrar_lugares_disponiveis())

evento.cancelar()
print(evento.mostrar_lugares_disponiveis())
