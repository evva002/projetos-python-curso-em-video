texto = 'Desafio 081'
print('{:=^30}'.format(texto))

numeros = []
cinco_lista = False

while True:
    print('=' * 30)
    escolha = str(input('Deseja adicionar um número à lista [S/N]: ')).upper()
    print('=' * 30)

    if escolha == 'N':
        print('Adeus!')
        print('=' * 30)
        break 
        
    elif escolha == 'S':
        num = int(input('digite o número: '))
        numeros.append(num)
    else:
        print('Escolha incorreta, tente novamente!')

if 5 in numeros:
    cinco_lista = True

print(f'O total de elementos digitados foi: {len(numeros)}')
print(f'O número cinco está na lista? {cinco_lista}')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é: {numeros}')

input("Pressione <enter> para encerrar!")