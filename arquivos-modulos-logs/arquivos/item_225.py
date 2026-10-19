"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 25
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import shutil
for i in range(0,10):
  nome_pasta = "pasta" + str(i)
  try:
    shutil.rmtree(nome_pasta)
  except:
    print("Falha ao excluir a pasta", nome_pasta)
