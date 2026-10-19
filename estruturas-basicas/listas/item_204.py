"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except IndexError as erro1:
  print("Erro de acesso ao ídice: "+ str(erro1))
except Exception as erro2:
  print("Ocorreu outro erro: "+str(erro2))

print("Fim")
