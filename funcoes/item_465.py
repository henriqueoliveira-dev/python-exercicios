"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 29
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

def menor(*numeros):
  menor = numeros[0]
  for i in numeros:
    menor = min(i, menor)
    return menor

print(menor(1,2,3,4,4,19,80,-2))
