"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 37
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import json
dicionario = None
with open('dados.json', 'rt') as arquivo:
  arquivo_lido = arquivo.read()
  dicionario = json.loads(arquivo_lido)

print(dicionario)
print(type(dicionario))
print(dicionario['Rodrigo']['Idade'])
