import random

texto = 'Desafio 019'
print('{:=^30}'.format(texto))

lista_alunos = ['Carlos', 'Joao', 'Maria', 'Elisabete']
print(f'O aluno escolhido foi: {random.choice(lista_alunos)}')

input("Pressione <enter> para encerrar!")