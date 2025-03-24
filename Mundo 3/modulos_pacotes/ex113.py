def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 113')

def leiaFloat():
    while True: 
        try:
            numero = input('Digite um número float: ')
            numero = float(numero.replace(',', '.'))
            return numero
        except (ValueError, TypeError):
            print('ATENÇÃO! Número inteiro digitado incorreto, tente novamente.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor.')
            numero = 0
            return numero 
      
def leiaInt():
    while True:
        try:
            numero = input('Digite um número inteiro: ')    
            numero = int(numero)
            return numero
        except (ValueError, TypeError):
            print('ATENÇÃO! Número inteiro digitado incorreto, tente novamente.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor.')
            numero = 0
            return numero 

num_inteiro = leiaInt()
num_float = leiaFloat()
print(f'O número inteiro digitado foi {num_inteiro} e o float foi {num_float}.')

input("Pressione <enter> para encerrar!")
