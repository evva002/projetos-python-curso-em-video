texto = 'Desafio 050'
print('{:=^30}'.format(texto))

soma = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(f'A soma somente dos números pares é: {soma}')

input("Pressione <enter> para encerrar!")   


