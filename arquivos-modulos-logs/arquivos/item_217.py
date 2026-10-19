"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 12
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import os
if os.path.exists("exemplo.txt"):
  os.remove("exemplo.txt")
else:
  print("O arquivo não existe")
#
