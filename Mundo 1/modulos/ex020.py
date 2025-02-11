import random

texto = 'Desafio 020'
print('{:=^30}'.format(texto))

lista_alunos = ['Carlos', 'Joao', 'Maria', 'Elisabete']
random.shuffle(lista_alunos)
print(f'A ordem gerada foi: {lista_alunos}')

input("Pressione <enter> para encerrar!")