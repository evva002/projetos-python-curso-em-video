import math

texto = 'Desafio 016'
print('{:=^30}'.format(texto))

num = float(input('Digite um número float: '))
print(f'A parte inteira do número digitado é: {math.trunc(num)}')

input("Pressione <enter> para encerrar!")