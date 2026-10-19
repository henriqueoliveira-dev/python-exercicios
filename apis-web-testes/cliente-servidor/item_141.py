"""Conteúdo extraído de: 03_Servidor.ipynb_10Dtr72D.ipynb
Célula original: 4
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

from flask import jsonify, Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def padrao():
  return 'Escolha um dos métodos'

@app.route('/cotacao/')
def cotacao():
    return '5.34'

@app.route('/conversao/<float:val>')
def conversao(val):
    return str(val * 5.34)

@app.route('/cotacaocompleta', methods=['GET'])
def cotacaocompleta():
    argumentos = request.args
    valor = float(argumentos.get('valor'))
    mes = argumentos.get('mes')

    total = 0.0
    if mes == 'janeiro':
      total = valor * 5.34
    elif mes == 'fevereiro':
      total = valor * 5.22
    elif mes == 'marco':
      total = valor * 5.19

    return str(total)

@app.route('/tabela/')
def tabele():
  return jsonify({'janeiro': 5.34, 'fevereiro': 5.22, 'marco': 5.19})

app.run()
