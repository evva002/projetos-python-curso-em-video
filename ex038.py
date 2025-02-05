texto = 'Desafio 038'
print('{:=^30}'.format(texto))

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro valor é maior: {num1:.2f}')
elif num2 > num1:
    print(f'O segundo valor é maior: {num2:.2f}')
else:
    print(f'Não existe valor maior, os dois números são iguais: {num1:.2f} e {num2:.2f}')