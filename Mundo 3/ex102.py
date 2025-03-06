def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 102'
titulo(texto)

def fatorial(numero, mostrar=False):
    fatorial_intern = 1
    if numero == 0:
        print(f'O fatorial de {numero} é: ', end='')
    elif mostrar == True:
        while numero > 0:
            print(f'{numero}', end='')
            print(' X ' if numero > 1 else ' = ', end='')
            fatorial_intern *= numero
            numero -= 1
    else:
        while numero > 0:
            fatorial_intern *= numero
            numero -= 1
    print(fatorial_intern)
       
fatorial(5)