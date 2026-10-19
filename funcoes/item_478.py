"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 13
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def print_str(texto, indice):
  if indice >= len(texto):
    return
  print(texto[indice])
  print_str(texto, indice + 1)

print_str("Python", 0)
