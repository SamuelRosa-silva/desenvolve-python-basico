#dados
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

#construindo a lista de aprovados usando compreensão de listas
aprovados = [
    aluno for aluno, nota in zip(alunos, notas)
    if nota >= 60
]

#imprimindo a lista de aprovados
print(aprovados)
