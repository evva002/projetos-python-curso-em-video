from random import randint

texto = 'Desafio 068'
print('{:=^30}'.format(texto))

vitorias_jogador = 0
vitorias_maquina = 0

while vitorias_maquina == 0:

    print('-=' * 10)
    print('JOGO DO PAR OU ÍMPAR')
    print('-=' * 10)
    escolha_jogador = str(input('Escolha par ou ímpar [P / I]: ')).upper().strip()
    numero_jogador = int(input('Digite um valor entre 0 e 10: '))
    numero_maquina = randint(0, 10)

    if escolha_jogador == 'P':
        soma = numero_jogador + numero_maquina
        
        #JOGADOR VENCE COM PAR
        if soma % 2 == 0:
            resultado = 'par'
            print(f"""Você jogou {numero_jogador} e a máquina jogou {numero_maquina}
Total de {soma} e deu {resultado}""")
            print('-=' * 10)
            print('VOCÊ VENCEU!')
            vitorias_jogador += 1
        
        #MÁQUINA VENCE COM IMPAR
        else:
            resultao = 'ímpar'
            print(f"""Você jogou {numero_jogador} e a máquina jogou {numero_maquina}
Total de {soma} e deu {resultado}""")
            print('-=' * 10)
            print('VOCÊ PERDEU!')
            vitorias_maquina += 1

    elif escolha_jogador == 'I':
        soma = numero_jogador + numero_maquina
        
        #MÁQUINA VENCE COM PAR
        if soma % 2 == 0:
            resultado = 'par'
            print(f"""Você jogou {numero_jogador} e a máquina jogou {numero_maquina}
Total de {soma} e deu {resultado}""")
            print('-=' * 10)
            print('VOCÊ PERDEU!')
            vitorias_maquina += 1
        
        #JOGADOR VENCE COM IMPAR
        else:
            resultado = 'ímpar'
            print(f"""Você jogou {numero_jogador} e a máquina jogou {numero_maquina}
Total de {soma} e deu {resultado}""")
            print('-=' * 10)
            print('VOCÊ VENCEU!')
            vitorias_jogador += 1
    
    #ESCOLHA DIFERENTE DE P OU I
    else:
        print('Escolha incorreta, digite novamente!')

print('-=' * 10)
print(f'Você ganhou um total de {vitorias_jogador} vezes.')
print('-=' * 10)

input("Pressione <enter> para encerrar!")