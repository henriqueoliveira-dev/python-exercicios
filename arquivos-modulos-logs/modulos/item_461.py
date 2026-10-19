"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 21
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

from datetime import datetime, timedelta

deta_atual = datetime.now()
datfutura1 = deta_atual + timedelta(days=10)
datfutura2 = deta_atual + timedelta(days=20)
datfutura3 = deta_atual + timedelta(days=30)
datfutura4 = deta_atual + timedelta(days=40)

print(datfutura1)
print(datfutura2)
print(datfutura3)
print(datfutura4)
