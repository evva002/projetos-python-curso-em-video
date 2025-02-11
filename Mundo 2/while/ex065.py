texto = 'Desafio 065'
print('{:=^30}'.format(texto))

num = 0
total_num = 0
soma = 0
escolha = False
maior = 0
menor = 0

while not escolha:
    
    num = float(input('Digite um número para adicionar a conta da média ou digite [-1] para sair: '))
    if num == -1:
        escolha = True
    else:
        soma += num
        total_num += 1

        if menor == 0 and maior == 0:
            menor = num
            maior = num
        elif num < menor:
            menor = num
        elif num > maior:
            maior = num

media = soma / total_num

print(f'O total de números digitados foi {total_num} e a média entre eles foi: {media:.2f}')
print(f'O maior número digitado foi: {maior:.2f}')
print(f'O menor número digitado foi: {menor:.2f}')

input("Pressione <enter> para encerrar!")