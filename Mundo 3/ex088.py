import random
from time import sleep

texto = 'Desafio 088'
print('{:=^30}'.format(texto))

jogos = []
numeros = []
titulo = 'JOGO DA MEGA SENA'

print('=' * 30)
print(f'{titulo:^30}')
print('=' * 30)
escolha = int(input('Quantos jogos você quer fazer? '))
print('=' * 30)
print('=' * 5, f'SORTEANDO {escolha} JOGOS', '=' * 5)
print('=' * 30)
sleep(1)

for c in range(escolha):
    contador = 0
    while True:
        num = random.randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            contador+=1
        if contador >= 6:
            break
    numeros.sort()
    jogos.append(numeros)
    print(f'Jogo {c + 1}: {jogos[c]}')
    numeros.clear()
    sleep(1)

print('=' * 30)

input("Pressione <enter> para encerrar!")