texto = 'Desafio 079'
print('{:=^30}'.format(texto))
    
numeros = []

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
        if num in numeros:
            print('Número já cadastrado, tente novamente!')    
        else:
            numeros.append(num)
    else:
        print('Escolha incorreta, tente novamente!')

numeros.sort()
print(f'Os números digitados em ordem foram: {numeros}')
print('=' * 30)

input("Pressione <enter> para encerrar!")