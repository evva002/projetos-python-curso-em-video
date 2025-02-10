texto = 'Desafio 060'
print('{:=^30}'.format(texto))

num = int(input('Digite um número inteiro: '))
fatorial = 0

if num == 0:
    print(f'O fatorial de {num} é 1.')

total = num * (num - 1)
num -= 2

while num > 0:
    fatorial += total * num 
    total = fatorial
    num -= 1

print(fatorial)