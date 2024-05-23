import random
alunos=['alisson', 'yasmin', 'pedro', 'lucas', 'mariana']
print(f"lista: {alunos}")
# embaralhar a lista
random.shuffle(alunos)
print(f"lista embaralhada: {alunos}")
# escolha um aluno aleatoriamente
aluno_sorteado = random.choice(alunos)
print(f"aluno sorteado: {aluno_sorteado}")

