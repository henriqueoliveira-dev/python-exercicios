"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 30
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

def meses():
  meses = ['Janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto', 'setembro','outubro','novembro','dezembro']
  for mes in meses:
    yield mes

for mes in meses():
  print(mes)
#
