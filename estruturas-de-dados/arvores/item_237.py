"""Conteúdo extraído de: 09_Ler_e_Escrever_Arquivos_.ipynb_1kwdhiR4.ipynb
Célula original: 45
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

dados ={
    'Rodrigo': {
         'CPF': '468290292',
         'SEXO':'M',
         'Endereço': 'Casa Miliden 2323',
         'Idade': 23
    },
    'Maria': {
         'CPF': '468290292',
         'SEXO':'F',
         'Endereço': 'Casa Rayzen 23',
         'Idade': 26,
         'Filhos': ['Ana', 'João']
    },
    'Pedro': {
         'CPF': '468290292',
         'SEXO':'M',
         'Endereço': 'Casa Miliden 2323',
         'Idade': 23
    }
}

raiz = xml.Element("DadosPessoais")

for key in dados:
  nome = key
  dados_pessoa = dados[key]
  cpf = dados_pessoa['CPF']
  sexo = dados_pessoa['SEXO']
  endereco = dados_pessoa['Endereço']
  idade = dados_pessoa['Idade']

  # A função criarTagPessoa já anexa 'pessoa' à 'raiz'
  pessoa = criarTagPessoa(raiz, nome, cpf, sexo, endereco, str(idade))

  if 'Filhos' in dados_pessoa:
    tag_filhos = xml.SubElement(pessoa, 'Filhos')
    # Iteramos sobre a lista de nomes que está no dicionário
    for filho in dados_pessoa['Filhos']:
      no_filho = xml.SubElement(tag_filhos, 'Pessoa', attrib={'Nome': filho})

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xml', 'wb') as files:
  arvore.write(files, encoding='utf-8', xml_declaration=True)
