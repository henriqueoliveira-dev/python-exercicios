"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 14
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def fatorial(num):
  if num == 0:
    return 1
  return num * fatorial(num - 1)

print(fatorial(5))
