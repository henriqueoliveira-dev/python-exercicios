"""Conteúdo extraído de: 31_Fun_es.ipynb_1KjVe-4N.ipynb
Célula original: 16
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

def calculadora(num1, num2, operacao = "soma"):
 def soma(a,b):
  return a + b
 def subtrai(a,b):
  return a - b

  if (operacao == "soma"):
    return soma(num1, num2)
  elif (operacao == "subtrai"):
    return subtrai(num1, num2)

print(calculadora(2,1,"+"))
