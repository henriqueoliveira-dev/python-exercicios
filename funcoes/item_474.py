"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def retorna_multiplo (a,b,c):
  a += a
  b += b
  c += c

  return a,b,c

x,y,z = retorna_multiplo(1,2,3)
print(x,y,z)
