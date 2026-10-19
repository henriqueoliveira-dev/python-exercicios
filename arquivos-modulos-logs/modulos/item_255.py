"""Conteúdo extraído de: 11_Modulos.ipynb_1yHEL3XU.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

# Se ainda não tiver instalado:
# pip install pmdarima

import pmdarima as pm

# Temperaturas registradas ao longo dos dias
temperaturas = [
    22, 23, 21, 24, 25,
    24, 26, 27, 26, 28,
    29, 28, 30, 31, 30,
    32, 33, 32, 34, 35
]

# O modelo analisa os dados históricos
modelo = pm.auto_arima(
    temperaturas,
    seasonal=False,
    suppress_warnings=True
)

# Fazer previsão dos próximos 5 valores
previsao = modelo.predict(n_periods=5)

print("Temperaturas previstas:")
print(previsao)
