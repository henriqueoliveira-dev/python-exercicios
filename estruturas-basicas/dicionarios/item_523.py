"""Conteúdo extraído de: 32_Listas.ipynb_1taQNADp.ipynb
Célula original: 32
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

dados_maria = {
    'sexo': 'feminino',
    'cpf' : '123456789',
    'rg' : '123456654'
}
dados_joao = {
    'sexo': 'masculino',
    'cpf' : '987654321',
    'rg' : '777654321'
}
dados_ana ={
    'sexo': 'feminino',
    'cpf' : '1234568778',
    'rg' : '123456854'
}
dados_por_nome = {
    'maria': dados_maria,
    'joao': dados_joao,
    'ana': dados_ana
}


print(dados_por_nome['joao']['sexo'])
