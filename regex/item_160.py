"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re
texto = 'aaaaaa'
info = re.search('^(aa){2,3}$',texto)
if info != None:
  print('Encontrado ocorrêcia em', info.span())
  print('Encontrado ocorrêcia em', info.group())
else:
  print('Não achei')
