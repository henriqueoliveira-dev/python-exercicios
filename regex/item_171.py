"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 32
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

import re
texto = 'Terça-Feira'

info = re.search("^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta -Feira|Sexta-Feira|Sábado|Domingo)$", texto)

if info != None:
  print("Encontrada ocorrêcia em ", info.span())
  print("Encontrada ocorrêcia em ", info.group())
else:
  print("Não achei")
