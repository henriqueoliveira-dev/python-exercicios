"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 47
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import xml.etree.ElementTree as xml
tree = xml.parse("dados_exemplo2.xml")
root = tree.getroot()
print(root.tag)

for pessoa in root:
  print(' ', pessoa.tag, pessoa.attrib['Nome'])
  for filho in pessoa:
    if (filho.tag == 'Filhos'):
      for neto in filho:
        print('  ', neto.tag, neto.attrib['Nome'])
    else:
      print('  ', filho.tag, filho.text)
