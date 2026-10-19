"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 24
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def anos():
  for i in range(2020,2030):
    yield str(i)

lestras = '-'.join(anos())
print(lestras)
