"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 17
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import datetime

data_completa = datetime.datetime.now()

data = data_completa.date()
hora = data_completa.time()

print(data)
print(hora)
