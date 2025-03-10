texto = 'Desafio 085'
print('{:=^30}'.format(texto))

numeros = [[], []]

for c in range(7):
    num = int(input(f'Digite o {c + 1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')
print('=' * 30)

input("Pressione <enter> para encerrar!")