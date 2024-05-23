import random
alunos=['alisson', 'yasmin', 'pedro', 'lucas', 'mariana']
print(f"lista: {alunos}")
# embaralhar a lista
random.shuffle(alunos)
print(f"lista embaralhada: {alunos}")
#ordena a lista crescente
alunos.sort()
print(f"lista crescente: {alunos}")
# ordena a lista decrescente
alunos.sort(reverse=True)
print(f"lista decrescente: {alunos}")
