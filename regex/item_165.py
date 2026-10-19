"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 22
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re

texto = '0 Cº'

info = re.search('(-)?[0-9]+ Cº$', texto)

if info != None:
  print("Temperatura válida")
else:
  print("Temperatura inválida")
