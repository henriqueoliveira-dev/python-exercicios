"""Conteúdo extraído de: 07_Interadores.ipynb_1y_yy4Sx.ipynb
Célula original: 17
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

produtos = [
['carro', '200.00'],
['cadeira','1000'],
['morto', '33000'],
['geladeira','2000'],
['armario','1500']
]

for produto, valor in produtos:
  print(f"{produto:<15} R$ {float(valor):>5.2f}")
