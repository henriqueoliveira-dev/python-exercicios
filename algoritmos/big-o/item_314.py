"""Conteúdo extraído de: 13_C_pia_de_Nota_o_Big-O.ipynb_1-Btboet.ipynb
Célula original: 50
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)

def combination(n):
  # O(1)
  print(n[0])

  # O(5)
  for i in range(5):
    print('test ', i)

  # O(n)
  for i in n:
    print(i)

  # O(n)
  for i in n:
    print(i)

  # O(3)
  print('Python')
  print('Python')
  print('Python')
