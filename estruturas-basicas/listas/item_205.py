"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 11
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("Inicio")
lista = [1,2,3]
numero = 10
try:
  dicisao = 10/ numero
  print(lista[12])
except IndexError as erro1:
  print("Erro de acesso ao ídice: "+ str(erro1))
except ZeroDivisionError  as erro2:
  print("Erro de disão por zero "+ str(erro2))
except Exception as erro3:
  print("Ocorreu outro erro: "+str(erro3))

print("Fim")
