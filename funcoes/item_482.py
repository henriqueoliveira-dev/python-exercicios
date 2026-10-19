"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 17
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def pegar_func_print():
  def print_var(var):
    print(var)
  return print_var

print_me = pegar_func_print()

print(10)
