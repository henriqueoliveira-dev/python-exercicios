"""Conteúdo extraído de: 26_POO-_Encapsulamento.ipynb_1QmMo6JF.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

class Pessoa:

  def __init__(self, nome, idade):

    self.nome = nome
    self.idade = idade

  def exibir_info(self):
      print(f"Informações da Pessoa:")
      print(f"Nome: {self.nome}")
      print(f"Idade: {self.idade}")


  def falar(self):
      print(f"{self.nome} está falando.")

class Estudante(Pessoa):

  def __init__(self, nome, idade, matricula):

      Pessoa.__init__(self, nome, idade)

      self.matricula = matricula

  def estudar(self):

      print(f"{self.nome} está estudado")

class Professor(Pessoa):

   def __init__(self, nome, idade, disciplina):

      Pessoa.__init__(self, nome, idade)

      self.disciplina = disciplina

   def ministrar_aula(self):

      print(f"{self.nome} está ministrando aula de {self.disciplina}")

#Criaçao objeto

pessoa = Pessoa("Alice", 30)

estudante = Estudante("Bob", 20, "12345")

professor = Professor("Carlos", 40, "Matemática")

#Exibindo infomações

pessoa.exibir_info()
print("")
estudante.exibir_info()
estudante.estudar()
print("")
professor.exibir_info()
professor.ministrar_aula()
