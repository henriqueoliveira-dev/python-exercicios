"""Conteúdo extraído de: 12_Big-O.ipynb_1_VaRqNN.ipynb
Célula original: 22
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

plt.figure(figsize=(10,8))
plt.ylim(1,100)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
