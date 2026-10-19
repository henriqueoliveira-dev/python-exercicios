"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 24
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import os
for i in range(0,10):
  nome_pasta = "pasta" + str(i)
  try:
    os.remove(nome_pasta + '/texto.txt')
  except:
    pass

  try:
    os.rmdir(nome_pasta)
  except:
    print("Falha ao excluir a pasta", nome_pasta)
    pass
