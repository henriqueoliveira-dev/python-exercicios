"""Conteúdo extraído de: 32_Listas.ipynb_1taQNADp.ipynb
Célula original: 57
Origem registrada no manifesto: Drive
Tipo: 🎯 Exercício
"""

obejetos = {
    'Cadeira' : ' Serve para sentar',
    'Monitor' : 'Serve para visualizar o processamento',
    'Mouse'   : 'Serve para realizar operações'
}
obejeto_procurado = input("Digite o objeto que você procura: ")
if obejeto_procurado in obejetos:
  print(obejetos[obejeto_procurado])
else:
  print("Objeto não encontrado")
