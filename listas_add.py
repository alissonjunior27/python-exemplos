aluno = ['alisson']
aluno.append('junin')
while True:
    nome = input('digite o nome do aluno: ')
    aluno.append(nome)
    resposta = input('deseja adicionar mais um aluno? (s/n): ')
    if resposta.upper() == 'N':
        break
print(f"alunos cadastrados: {aluno}")
