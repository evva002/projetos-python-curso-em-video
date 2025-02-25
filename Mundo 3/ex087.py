texto = 'Desafio 087'
print('{:=^30}'.format(texto))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
terceira_linha = 0

for l in range(3):
    for c in range(3):
        num = int(input(f'Digite um número para [{l}, {c}]: '))
        matriz[l][c] = num
        if num % 2 == 0:
            soma_pares += num
        if l == 2:
            terceira_linha += num
        
segunda_linha = max(matriz[1])

print('=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=' * 30)

print(f'A soma dos números pares é: {soma_pares}')
print(f'O maior valor da segunda linha é: {segunda_linha}')
print(f'A soma dos valores da terceira linha é: {terceira_linha}')

input("Pressione <enter> para encerrar!")