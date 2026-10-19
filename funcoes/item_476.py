"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 11
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def multiplica(y):
  return lambda x : x * y

dobro = multiplica(2)
triplo = multiplica(3)

print(dobro(11))
print(triplo(11))
#
