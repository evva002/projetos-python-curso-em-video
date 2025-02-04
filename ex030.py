texto = 'Desafio 030'
print('{:=^30}'.format(texto))

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar')