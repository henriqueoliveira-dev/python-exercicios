"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 11
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def sort_por_tamanho(item):
  return len (item)

lista = ["a","b","ab","de","abcd","abcd"]

lista.sort(key=sort_por_tamanho)
print(lista)
