"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 19
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def DeixaMaisculo(func):
  def inner_func():
    return func().upper()
  return inner_func

@DeixaMaisculo
def retorna_string():
  return "string de teste"

valor = retorna_string()
print(valor)
