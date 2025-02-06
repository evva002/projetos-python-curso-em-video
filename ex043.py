texto = 'Desafio 043'
print('{:=^30}'.format(texto))

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura (0.00): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso.')
    print(f'IMC: {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
    print(f'IMC: {imc:.2f}')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
    print(f'IMC: {imc:.2f}')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
    print(f'IMC: {imc:.2f}')
else:
    print('Obesidade mórbida.')
    print(f'IMC: {imc:.2f}')

input("Pressione <enter> para encerrar!")