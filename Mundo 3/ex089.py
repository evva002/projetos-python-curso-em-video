texto = 'Desafio 089'
print('{:=^30}'.format(texto))

alunos = []
aluno = []
media = 0.0

while True:
    print('=' * 30)
    escolha = str(input('Deseja cadastrar um aluno [S/N]? ')).upper()
    print('=' * 30)
    if escolha == 'N':
        break
    elif escolha == 'S':
        aluno.append(str(input('Nome: ').upper()))
        aluno.append(float(input('Nota 1: ')))
        aluno.append(float(input('Nota 2: ')))
        aluno.append((aluno[1] + aluno[2]) / 2) 
        alunos.append(aluno[:])
        aluno.clear()
    else:
        print('Escolha incorreta, tente novamente!')

print('=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
for i, c in enumerate(alunos):
    print(f'{i:<4}{alunos[i][0]:<10}{alunos[i][3]:>7.2f}')
print('=' * 30)

while True:
    escolha = int(input('Mostrar nota de qual aluno? [999 interrompe]:  '))
    if escolha == 999:
        print('=' * 30)
        break
    elif escolha >= len(alunos):
        print('=' * 30)
        print('Escolha incorreta, tente novamente!')
        print('=' * 30)
    else:
        print('=' * 30)
        print(f'Notas de {alunos[escolha][0]} são: [{alunos[escolha][1]:.2f}] e [{alunos[escolha][2]:.2f}]')
        print('=' * 30)

input("Pressione <enter> para encerrar!")