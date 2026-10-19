"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 7
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re
texto = 'ABCDefHI123'

info1 = re.findall('[a-z]',texto)
info2 = re.findall('[A-Z]',texto)
info3 = re.findall('[0-9]',texto)
info4 = re.findall('[a-zA-Z0-9]',texto)

print(info1)
print(info2)
print(info3)
print(info4)
#
