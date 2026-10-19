"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 41
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import xml.etree.ElementTree as xml
from xml.dom import minidom
import os

no_raiz = xml.Element("DadosPessoais")
no_pessoa = xml.SubElement(no_raiz, "Pessoa", attrib={'Nome':'Rodrigo'})

no_cpf = xml.SubElement(no_pessoa, 'CPF')
no_cpf.text = '468290292'

no_sexo = xml.SubElement(no_pessoa, 'SEXO')
no_sexo.text = 'M'

no_endereco = xml.SubElement(no_pessoa, 'Endereço')
no_endereco.text = 'Casa Miliden 2323'

no_idade = xml.SubElement(no_pessoa, 'Idade')
no_idade.text = '23'

# Convertemos o elemento XML em uma string de bytes
xml_string = xml.tostring(no_raiz, encoding='utf-8')

# Usamos o minidom para formatar com recuo e quebras de linha
xml_formatado = minidom.parseString(xml_string).toprettyxml(indent="  ")

# Salvamos a string formatada no arquivo
with open('dados_exemplo.xml', 'w', encoding='utf-8') as files:
  files.write(xml_formatado)
