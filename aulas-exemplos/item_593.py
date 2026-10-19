"""Conteúdo extraído de: 36_1Fundamentos-2.ipynb_1NZc_BNa.ipynb
Célula original: 15
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

ovos = 56
pessoas = 3
print("Tenho inicialmete %d ovos para %d pessoas " % (ovos,pessoas))
ovos_por_pessoas = ovos // pessoas
ovos_restantes = ovos % pessoas
print("Cada pessoa receberá %d ovos e sobrará %d ovos" % (ovos_por_pessoas,ovos_restantes))
print("Restou %d ovos que não puderam serem divididos " % (ovos_restantes))
