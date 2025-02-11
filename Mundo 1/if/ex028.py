import random

texto = 'Desafio 028'
print('{:=^30}'.format(texto))

numero_usuario = int(input('Digite um número inteiro de 0 a 5: '))
numero_random = random.randint(0, 5)
print(f'Número gerado de forma aleatória: {numero_random}')
if numero_usuario == numero_random:
    print('Parabéns, você acertou!')
else:
    print('Poxa, você errou :/')

input("Pressione <enter> para encerrar!")