"""Conteúdo extraído de: 🐍 200 QUESTÕES DE PYTHON — TRILHA CUMULATIVA.ipynb
Célula original: 93
Origem registrada no manifesto: ZIP
Tipo: 🎯 Exercício
"""

alunos = [
    {"nome": "Henrique", "nota": 8.9, "situacao": "aprovado"},
    {"nome": "Enzo", "nota": 7.7, "situacao": "aprovado"},
    {"nome": "Maria", "nota": 9.9, "situacao": "aprovado"},
    {"nome": "Karina", "nota": 5.5, "situacao": "reprovado"},
    {"nome": "Kevin", "nota": 3, "situacao": "reprovado"}
]

for aluno in alunos:
    if aluno["nota"] <= 7:
        print(
            f"Aluno: {aluno['nome']:<10}"
            f"Nota: {aluno['nota']:<6}"
            f"Situação: Reprovado"
        )
