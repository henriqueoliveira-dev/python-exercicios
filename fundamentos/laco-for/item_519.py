"""Conteúdo extraído de: 32_Listas.ipynb_1taQNADp.ipynb
Célula original: 28
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

idades = {'ana': 10, 'joao': 20, 'maria': 30, 'fernado':'indefirido' }
listas = idades.items()
print(listas, end = '\n \n')
for item in listas:
  print(item[0], item[1])
