"""Conteúdo extraído de: 06_Expres_o_Regulares.ipynb_1aoFwGsr.ipynb
Célula original: 9
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import re
texto = 'ABCDefHI123'
info = re.findall('[A-Z]|[0-9]', texto)
print(info)
