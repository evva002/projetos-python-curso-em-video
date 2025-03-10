def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 102')

def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('=' * tamanho)
    print(f'  {mensagem}')
    print('=' * tamanho)


def manual():
    from time import sleep
    while True:
        escreva('SISTEMA DE AJUDA HELP')
        escolha = str(input('Função ou biblioteca: ')).lower()
        if escolha == 'sair':
            print('=' * 30)
            print('Até mais!')
            print('=' * 30)
            break
        else:
            sleep(1)
            print('=' * 30)
            print(f'Acessando manual do comando {escolha}')
            print('=' * 30)
            sleep(1)
            help(escolha)
manual()

input("Pressione <enter> para encerrar!")