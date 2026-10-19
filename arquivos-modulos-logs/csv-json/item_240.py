"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 52
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import yaml

# Abre o arquivo YAML para leitura
with open('/content/config.yaml', 'r', encoding='utf-8') as arquivo:
    # Carrega o conteúdo do arquivo usando o safe_load para maior segurança
    dados_yaml = yaml.safe_load(arquivo)

# Exibe o conteúdo lido (que agora é um dicionário comum do Python)
print("Conteúdo do YAML lido:")
import pprint
pprint.pprint(dados_yaml)
