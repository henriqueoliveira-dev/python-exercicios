"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 54
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

import yaml

caminho_yaml = "config.yaml"

# 1. Carrega o arquivo existente
try:
    with open(caminho_yaml, 'r', encoding='utf-8') as f:
        dados = yaml.safe_load(f)
except FileNotFoundError:
    dados = {}

# Se o arquivo estiver vazio, inicializa como um dicionário vazio
if dados is None:
    dados = {}

# 2. Acrescenta as novas informações desejadas
# Se a seção 'database' não existir, nós a criamos
if 'database' not in dados:
    dados['database'] = {}

dados['database']['name'] = 'meu_banco_de_dados'
dados['database']['user'] = 'admin'
dados['database']['password'] = 'senha123'

# 3. Salva os dados atualizados de volta no arquivo
with open(caminho_yaml, 'w', encoding='utf-8') as f:
    yaml.safe_dump(dados, f, default_flow_style=False, allow_unicode=True)

print("Informações salvas e atualizadas com sucesso no YAML!")

# Mostra como o arquivo ficou estruturado
with open(caminho_yaml, 'r', encoding='utf-8') as f:
    print(f.read())
