texto = 'Desafio 080'
print('{:=^30}'.format(texto))

numeros = []

for c in range(5):
    num = int(input('Digite um número: '))

    if c == 0 or num > max(numeros):
        numeros.append(num)
        print('O número foi adicionado ao final da lista')
        print('=' * 30)
    else:
        posicao = 0
        while posicao < len(numeros):
            if num <= numeros[posicao]:
                numeros.insert(posicao, num)
                print(f'O número foi adicionado na posição {posicao + 1}')
                print('=' * 30)
                break
            posicao += 1

print(f'Lista em ordem crescente: {numeros}')
print('=' * 30)

input("Pressione <enter> para encerrar!")