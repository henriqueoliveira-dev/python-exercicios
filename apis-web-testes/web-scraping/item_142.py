"""Conteúdo extraído de: 04_Cliente.ipynb_1B0X8XsK.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

import requests
x = requests.get('http://armchair-darkening-overtime.ngrok-free.dev/cotacao/')
print(x.text)
print(x)
