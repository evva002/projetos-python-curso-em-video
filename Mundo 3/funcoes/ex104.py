def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 104')

def leiaInt():
    numero = input('Digite um número: ')
    if numero.isdigit():
        print(f'Você digitou o número {numero}.')
    else:
        while numero != numero.isdigit():
            numero = input('Por favor digite um número correto: ')
            if numero.isdigit():
                print(f'Você digitou o número {numero}.')
                break
        
leiaInt()

input("Pressione <enter> para encerrar!")