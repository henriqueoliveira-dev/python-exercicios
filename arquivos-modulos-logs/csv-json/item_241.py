"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 53
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import yaml

with open("config.yaml") as f:
  data = yaml.load(f, Loader=yaml.FullLoader)

  # Evita o erro se o arquivo YAML estiver vazio (None)
  if data is None:
    data = {}

  # Verifica se a chave 'database' existe antes de acessar
  if 'database' in data:
    print(data['database']['name'])
  else:
    print("A chave 'database' não foi encontrada no arquivo YAML.")
