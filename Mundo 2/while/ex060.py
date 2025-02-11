texto = 'Desafio 060'
print('{:=^30}'.format(texto))

num = int(input('Digite um número inteiro: '))
fatorial = 1
num_inicial = num

if num == 0:
    print(f'O fatorial de {num} é 1.')

while num > 0:
    fatorial *= num 
    num -= 1

print(f'O fatorial de {num_inicial}! é {fatorial}')