"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 34
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import json
idades = {
    'Rogéro': 20,
    'Maria':34,
    'Pedro':18
}

print(json.dumps(idades, ensure_ascii=False))
#ensure_ascii=False = converte o caracter para não dar erro na coplagem
