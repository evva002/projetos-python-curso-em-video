texto = 'Desafio 078'
print('{:=^30}'.format(texto))

numeros = []

for c in range(5):
    numeros.append(int(input(f'Digite o {c + 1}º número: ')))

print(f'A lista criada foi: {numeros}')
print(f'O maior número digite é {max(numeros)} e suas posições são: ', end='')
for c in range(5):
    if max(numeros) == numeros[c]:
        print(f'...{c + 1}', end='')
print(f'\nO menor número digite é {min(numeros)} e suas posições são: ', end='')
for c in range(5):
    if min(numeros) == numeros[c]:
        print(f'...{c + 1}', end='')

input("\nPressione <enter> para encerrar!")