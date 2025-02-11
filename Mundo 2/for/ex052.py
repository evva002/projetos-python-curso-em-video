texto = 'Desafio 052'
print('{:=^30}'.format(texto))

num = int(input('Digite um número: '))
total_divisoes = 0

for c in range(1, num + 1):
    if num % c == 0:
        total_divisoes += 1
print(f'Total de divisores: {total_divisoes}')
if total_divisoes == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')

input("Pressione <enter> para encerrar!")