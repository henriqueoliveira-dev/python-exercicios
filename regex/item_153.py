"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 8
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re
texto = 'existem 64 predios com 700 metros'
# |  equivalente ao 'or'.
info = re.findall('predios|metros', texto)
print(info)
