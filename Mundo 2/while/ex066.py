texto = 'Desafio 066'
print('{:=^30}'.format(texto))

num = 0
total = 0
soma = 0

while True:
    num = int(input('Digite um número para adicionar a conta (ou digite [999] para sair): '))
    if num == 999:
        break
    else:
        soma += num 
        total += 1

print(f'O total de números digitados foi {total} e a soma entre eles é: {soma}')

input("Pressione <enter> para encerrar!")