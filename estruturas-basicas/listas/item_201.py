"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except:
  print("Falha do acessar, linha não encontrada")
finally:
  del lista
  print("Executa sempre que o try-exept acabar, mesmo que não o corra erro")
  print("fim")
