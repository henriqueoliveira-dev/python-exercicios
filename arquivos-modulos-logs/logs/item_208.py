"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 16
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("inicio")
lista = [1,2,3]
try:
  print(lista[10])
except IndexError as erro1:
  custom_logger("error","indiíce incorreto!")

custom_logger("info","fim do progrma")
