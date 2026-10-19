"""Conteúdo extraído de: 33_Estrutura_de_Programma_ao-_FOR_.ipynb_1bHs91e0.ipynb
Célula original: 9
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

letra = input("Digite uma letra: ")

texto = input("Digite um texto: ")

for i in range(0, len(texto)):
  if letra == texto[i]:
    print("Encontre a letra \'%s\' na possição %d " % (letra, i))
