texto = 'Desafio 033'
print('{:=^30}'.format(texto))

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1}')
    if num2 > num3:
        print(f'O menor número é o {num3}')
    else:
        print(f'O menor número é o {num2}')

elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}')
    if num1 > num3:
        print(f'O menor número é o {num3}')
    else:
        print(f'O menor número é o {num1}')

else:
    print(f'O maior número é o {num3}')
    if num1 > num2:
        print(f'O menor número é o {num2}')
    else:
        print(f'O menor número é o {num1}')