"""Conteúdo extraído de: 04_Cliente.ipynb_1B0X8XsK.ipynb
Célula original: 3
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import requests
x = requests.get('http://armchair-darkening-overtime.ngrok-free.dev/cotacaocompleta?valor=200&mes=marco')
print(x.text)
print(x)
