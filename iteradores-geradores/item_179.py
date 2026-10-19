"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 10
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def meu_range(num):
  local_num = 1
  while local_num < num:
    yield local_num
    local_num += 1

for num in meu_range(10):
  print(num)
#
