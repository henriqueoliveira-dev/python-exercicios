"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 43
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import xml.etree.ElementTree as xml
from xml.dom import minidom
import os

def criarTagPessoa(raiz, nome, cpf, sexo, endereco, idade):
  no_pessoa = xml.SubElement(raiz, "Pessoa", attrib={'Nome': nome})

  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf

  no_sexo = xml.SubElement(no_pessoa, 'SEXO')
  no_sexo.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereço')
  no_endereco.text = endereco

  no_idade = xml.SubElement(no_pessoa, 'Idade')
  no_idade.text = idade

  return no_pessoa

raiz = xml.Element("DadosPessoais")
pessoa1 = criarTagPessoa(raiz, "Rodrigo", "468290292", "M", "Casa Miliden 2323", "23")
pesso2 = criarTagPessoa(raiz, "Maria", "468290292", "F", "Casa Rayzen 23", "26")
pesso3 = criarTagPessoa(raiz, "Pedro", "468290292", "M", "Casa Miliden 2323", "23")

arvore = xml.ElementTree(raiz)

with open('dados_exemplo.xml', 'wb') as files:
  arvore.write(files, encoding='utf-8', xml_declaration=True)
