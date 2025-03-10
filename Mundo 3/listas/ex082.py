texto = 'Desafio 082'
print('{:=^30}'.format(texto))

numeros = []
numeros_pares = []
numeros_impares = []
while True:
    print('=' * 30)
    escolha = str(input('Deseja adicionar um número à lista [S/N]? ')).upper()
    print('=' * 30)
    if escolha == 'N':
        print('Adeus!')
        print('=' * 30)
        break
    elif escolha == 'S':
        num = int(input('Digite um número para adicionar à lista: '))
        numeros.append(num)
    else:
        print('Escolha incorreta, tente novamente!')

for c in numeros:
    if c % 2 == 0:
        numeros_pares.append(c)
    else:
        numeros_impares.append(c)

print(f'A lista digitada foi: {numeros}')
print(f'Os números pares digitados foram: {numeros_pares}')
print(f'Os números ímpares digitados foram: {numeros_impares}')

input("Pressione <enter> para encerrar!")