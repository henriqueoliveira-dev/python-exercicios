"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def print_num(num):
  print(num)
  if num >= 10:
    return
  print_num(num + 1)

print_num(0)
