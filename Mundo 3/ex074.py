from random import randint

texto = 'Desafio 074'
print('{:=^30}'.format(texto))

maior = -1
menor = -1
numeros = tuple(randint(0,10) for c in range(5))

for c in range(0, 5):

    if menor == -1 and maior == -1:
        maior = numeros[c]
        menor = numeros[c]

    elif numeros[c] < menor:
        menor = numeros[c]

    elif numeros[c] > maior:
        maior = numeros[c]

print(f'Tupla gerada aleatoriamente: {numeros}')
print(f'O maior número da tupla é: {maior}')
print(f'O menor número da tupla é: {menor}')

input("Pressione <enter> para encerrar!")