"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 28
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

import re
texto = '28'
info = re.search("([2][0-9])|([3][0-5])$", texto)
if info != None:
  print("Encontrada ocorrêcia em ", info.span())
  print("Encontrada ocorrêcia em ", info.group())
else:
  print("Não achei")
