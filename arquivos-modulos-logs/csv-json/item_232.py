"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 35
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import json
DadosPessoas ={
    'Rodrigo': {
         'CPF': '468290292',
         'SEXO':'M',
         'Endereço': 'Casa Miliden 2323',
         'Idade': 23
    },
    'Maria': {
         'CPF': '468290292',
         'SEXO':'F',
         'Endereço': 'Casa Rayzen 23',
         'Idade': 26,
         'Filhos': ['Ana', 'João']
    }

}

texto = json.dumps(DadosPessoas, indent=4, ensure_ascii=False)
print(texto)

with open('dados.json', 'w') as arquivo:
  arquivo.write(texto)
