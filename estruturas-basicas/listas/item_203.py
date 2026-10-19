"""Conteúdo extraído de: 08_GEST_O_E_EXECU_O_DE_LOG.ipynb_1TkwtV39.ipynb
Célula original: 9
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

print("Inicio")
lista = [1,2,3]
try:#codigo que pode dar erro
  print(lista[10])
except: #codigo executado se der erro
  print("Falha do acessar, linha não encontrada")
else: #codigo executado se não ser erro
  print("Não houve erro")
finally:#codigo executado sempre
  print("Executa sempre")
print("fim")
