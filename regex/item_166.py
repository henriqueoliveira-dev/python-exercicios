"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 23
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re

texto = '99224466'

info = re.search('^99([0-9]{6})$', texto)

if info != None:
  print("numero válida")
else:
  print("numero inválida")
