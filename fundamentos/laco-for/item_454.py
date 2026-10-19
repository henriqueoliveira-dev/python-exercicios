"""Conteúdo extraído de: 30_Fun_es_Builtin.ipynb_1imkqzgs.ipynb
Célula original: 13
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

produtos = [["carro","R 100.00"],["cadeira","1000.00"],["moto"],["40.000,00"],["galadeira","R$ 2000"]]
for item in produtos:
    if len(item) == 2:
        produto, valor = item
    else:
        produto = item[0]
        valor = None # Or some default value like 'N/A'
    print(produto, valor)
