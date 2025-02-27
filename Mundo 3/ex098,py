from time import sleep

def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 098'
titulo(texto)

def contagemUm():
    print('=' * 30)
    print('Contagem de 1 até 10 de 1 em 1')
    sleep(2)
    for c in range(1, 11):
        sleep(0.5)
        print(f'{c}', end=' ')
    sleep(1)
    print('FIM!')

def contagemDois():
    print('=' * 30)
    print('Contagem de 10 até 0 de 2 em 2')
    sleep(2)
    for c in range(10, -1, -2):
        sleep(0.5)
        print(f'{c}', end=' ')
    sleep(0.5)
    print('FIM!')

def contagemTres(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('=' * 30)
    print(f'Contagem de {inicio} até {fim} no passo {passo}')
    if inicio > fim and passo < 0:
        passo = abs(passo)
        while inicio >= fim:
            sleep(0.5)
            print(f'{inicio}', end='...')
            inicio -= passo
    elif inicio < fim:
        while inicio <= fim:
            sleep(0.5)
            print(f'{inicio}', end='...')
            inicio += passo
    elif inicio > fim:
        while inicio >= fim:
            sleep(0.5)
            print(f'{inicio}', end='...')
            inicio -= passo
    sleep(0.5)
    print('FIM!')

contagemUm()
contagemDois()
i = int(input('Digite o ínicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contagemTres(i, f, p)

input("Pressione <enter> para encerrar!")