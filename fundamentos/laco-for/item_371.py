"""Conteúdo extraído de: 25_Matrizes.ipynb_13eotzml.ipynb
Célula original: 6
Origem registrada no manifesto: Drive
Tipo: 🚀 Projeto/protótipo
"""

"""
Exemplo de Matrizes e Média de Notas

Você foi contratado para desenvolver um sistema simples de registro de
notas para uma escola. O professor possui 3 alunos e para cada um, ele
deseja registrar 4 notas correspondentes aos bimestres do ano letivo.

Tarefas:

    - Solicite ao usuário o nome de cada aluno.
    - Para cada aluno, solicite as 4 notas correspondentes.
    - Armazene todas essas informações em uma matriz, onde cada
        linha representa um aluno e as colunas contêm o nome do
        aluno seguido por suas 4 notas.
    - Calcule a média das notas de cada aluno.
    - Imprima o nome, as notas e a média de cada aluno.

Dicas:

    Utilize loops for para percorrer os alunos e as notas.
    Lembre-se de que a média é a soma das notas dividida pelo número total de notas.
    Mantenha a organização do código para facilitar a leitura e a correção.
"""

# Inicializa uma matriz vazia para armazenar os nomes e as notas dos alunos
matriz_alunos = []

# Inicia um loop para coletar informações de 3 alunos
for i in range(3):

    # Solicita o nome do aluno atual
    nome = input(f"Digite o nome do aluno {i + 1}: ")

    # Inicializa uma lista vazia para armazenar as notas do aluno atual
    notas = []

    # Inicia um loop para coletar as 4 notas do aluno atual
    for j in range(4):

        # Solicita a nota atual do aluno
        nota = float(input(f"Digite a nota {j + 1} do aluno {nome}: "))

        # Adiciona a nota coletada à lista de notas
        notas.append(nota)

    # Adiciona o nome do aluno e suas notas à matriz de alunos
    matriz_alunos.append([nome] + notas)


# Inicia um loop para imprimir as informações de cada aluno
for aluno in matriz_alunos:

    # Extrai o nome do aluno da lista atual
    nome = aluno[0]

    # Extrai as notas do aluno da lista atual
    notas = aluno[1:]

    # Calcula a média das notas do aluno
    media = sum(notas) / 4

    # Imprime as informações do aluno
    print("\n" + "-"*40)
    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")



"""
Em Python, uma matriz é frequentemente representada como
uma lista de listas, e a palavra "lista" é usada para se referir
à estrutura de dados básica de sequência em Python, que é
implementada como uma array dinâmica.

Quando dizemos "matriz" neste contexto, estamos nos referindo
a uma representação de uma matriz matemática. Então, matriz_alunos
é uma lista em Python, mas consideramos cada elemento dessa
lista (que também é uma lista) como uma linha da matriz.

Isso nos permite acessar e manipular elementos da matriz usando
dois índices: um para a linha e outro para a coluna.
"""
print()
