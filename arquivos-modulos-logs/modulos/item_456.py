"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import datetime
data = datetime.datetime.now()
hora = data.strftime("%H:%M:%S")
data = data.strftime("%d/%m/%Y")
print(hora)
print(data)
