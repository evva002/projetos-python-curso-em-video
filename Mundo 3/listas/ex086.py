texto = 'Desafio 086'
print('{:=^30}'.format(texto))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        num = int(input(f'Digite um número para [{l}, {c}]: '))
        matriz[l][c] = num

print('=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=' * 30)

input("Pressione <enter> para encerrar!")