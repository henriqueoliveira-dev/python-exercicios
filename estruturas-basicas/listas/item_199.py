"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 5
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except Exception as error:
  print("Falha do acessar, linha não encontrada, mensagem: " + str(error))
  print("fim")
