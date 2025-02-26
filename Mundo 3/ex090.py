texto = 'Desafio 090'
print('{:=^30}'.format(texto))

alunos = []
aluno = {}

aluno['nome'] = str(input('Nome aluno: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['resultado'] = 'Aprovado'
else:
    aluno['resultado'] = 'Reprovado'

alunos.append(aluno.copy())

print('=' * 30)
print(f'Nome aluno: {alunos[0]['nome']}')
print(f'Média aluno: {alunos[0]['media']}')
print(f'Situação aluno: {alunos[0]['resultado']}')
print('=' * 30)

input("Pressione <enter> para encerrar!")