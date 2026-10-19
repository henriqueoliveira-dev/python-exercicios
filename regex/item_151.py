"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re
texto = 'existem 64 predios com 700 metros'
info = re.search('predios',texto)
if info != None:
  print('Encontrado ocorrêcia em', info.span())
  print('Encontrado ocorrêcia em', info.group())
else:
  print('Não achei')
