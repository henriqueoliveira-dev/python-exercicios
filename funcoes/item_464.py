"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 27
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

def soma(num1, num2):
  soma = num1 + num2
  soma = min(10000,soma)
  soma = max(0,soma)
  return soma
print(soma(20,20))
print(soma(5000,6000))
print(soma(10,-20))
