"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 25
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

# DD/MM/AAAA
# O dia pode variar de 00 a 31
# O mês de 00 a 12
# O ano de 0000 a 9999

texto = '33/12/1998'

info = re.search('^([1-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$',texto)
if info != None:
  print('Data válida', info.span())
  print('Data Inválida', info.group())
else:
  print('Não achei')
