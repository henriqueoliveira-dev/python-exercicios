"""Conteúdo extraído de: 13_C_pia_de_Nota_o_Big-O.ipynb_1-Btboet.ipynb
Célula original: 37
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
  plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
