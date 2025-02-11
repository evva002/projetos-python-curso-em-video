import random
from time import sleep

texto = 'Desafio 045'
print('{:=^30}'.format(texto))

pontos_jogador = 0 
pontos_maquina = 0

while pontos_jogador < 2 and pontos_maquina < 2:
    print('MELHOR DE 3')
    print(f'Pontos jogador: {pontos_jogador}')
    print(f'Pontos máquina: {pontos_maquina}')
    print('-=' * 10)

    escolha_jogador = str(input("""Escolha entre:
[Pedra] [Papel] [Tesoura]
Sua escolha: """)).lower()

    print('-=' * 10)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=' * 10)

    jokenpo = ['pedra', 'papel', 'tesoura']
    escolha_maquina = random.choice(jokenpo)

    if escolha_jogador == escolha_maquina:
        print(f'Escolha do jogador: {escolha_jogador}')
        print(f'Escolha da máquina: {escolha_maquina}')
        print('-=' * 10)
        resultado = 'EMPATE'
        texto = '=-' * 5
        print(f'{texto}{resultado}{texto}')
        print('-=' * 10)

    elif escolha_jogador == 'pedra':
        if escolha_maquina == 'papel':
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ PERDEU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_maquina += 1
        else:
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ GANHOU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_jogador += 1

    elif escolha_jogador == 'papel':
        if escolha_maquina == 'tesoura':
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ PERDEU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_maquina += 1
        else:
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ GANHOU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_jogador += 1

    elif escolha_jogador == 'tesoura':
        if escolha_maquina == 'pedra':
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ PERDEU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_maquina += 1
        else:
            print(f'Escolha do jogador: {escolha_jogador}')
            print(f'Escolha da máquina: {escolha_maquina}')
            print('-=' * 10)
            resultado = 'VOCÊ GANHOU!'
            texto = '=-' * 5
            print(f'{texto}{resultado}{texto}')
            print('-=' * 10)
            pontos_jogador += 1
    else:
        print('Poxa, você não escolheu nenhuma opção válida. escolha novamente!')
        print('-=' * 10)

print('MELHOR DE 3')
print(f'Pontos jogador: {pontos_jogador}')
print(f'Pontos máquina: {pontos_maquina}')
print('-=' * 10)
if pontos_jogador == 2:
    print('PARABÉNS, VOCÊ VENCEU!!!')
else:
    print('A MÁQUINA VENCEU :(')
print('-=' * 10)


input("Pressione <enter> para encerrar!")