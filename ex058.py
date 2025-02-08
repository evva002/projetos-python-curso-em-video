import random

texto = 'Desafio 058'
print('{:=^30}'.format(texto))

acertou = False
numero_tentativas = 0

while not acertou:
    numero_usuario = int(input('Digite um número inteiro de 0 a 10: '))
    numero_random = random.randint(0, 10)
    print(f'Número gerado de forma aleatória: {numero_random}')
    
    if numero_usuario == numero_random:
        print('VOCÊ ACERTOU!')
        print(f'Número de tentativas até o acerto: {numero_tentativas}')
        acertou = True

    else:
        print('VOCÊ ERROU. Tente novamente!')
        numero_tentativas += 1

input("Pressione <enter> para encerrar!")