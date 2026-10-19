"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 22
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import os
for i in range(0,10):
  nome_pasta = "pasta" + str(i)
  try:
    os.mkdir(nome_pasta)
  except:
    pass

  try:
    caminho_arquivo = os.path.join(nome_pasta, 'texto.txt')
    open(caminho_arquivo, 'wt').close()
  except:
    pass
