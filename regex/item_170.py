"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 30
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

import re
texto = 'este notebook tiliza python'
info = re.search("python", texto)
if info != None:
  print("Encontrada ocorrêcia em ", info.span())
  print("Encontrada ocorrêcia em ", info.group())
else:
  print("Não achei")
