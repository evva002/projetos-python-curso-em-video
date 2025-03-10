from random import randint
from time import sleep

def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 100'
titulo(texto)

def sorteia():
    print('=' * 30)
    print(f'{'SORTEANDO NÚMEROS':^30}')
    print('=' * 30)
    sleep(1)
    numeros = []
    num = 0
    for c in range (5):
        num = randint(1, 100)
        print(f'{num}', end=' ')
        numeros.append(num)
        sleep(1)
    print()
    print('=' * 30)
    return numeros

def somaPar(*valores):
    soma_par = 0
    print(f'Somando os valores pares de {valores}...')
    sleep(2)
    for c in valores:
        if c % 2 == 0:
            soma_par += c
            print(f'{c} é par')
            sleep(1)
    print(f'A soma dos valores pares é: {soma_par}')

numeros_sorteados = sorteia()
somaPar(*numeros_sorteados)

print('=' * 30)
input("Pressione <enter> para encerrar!")