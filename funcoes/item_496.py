"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 38
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def func_pai():
  pai = 10

  def func_filho():
    nonlocal pai
    pai = 20

    print(pai)

  func_filho()
  print(pai)

func_pai()
