texto = 'Desafio 023'
print('{:=^30}'.format(texto))

num = input('Digite um número de 0 a 9999: ')

if len(num) == 4:
    num_milhar = num[0]
    num_centena = num[1]
    num_dezena = num[2]
    num_unidade = num[3]
    print(f'Unidade: {num_unidade}')
    print(f'Dezena: {num_dezena}')
    print(f'Centena: {num_centena}')
    print(f'Milhar: {num_milhar}')

elif len(num) == 3:
    num_milhar = 0
    num_centena = num[0]
    num_dezena = num[1]
    num_unidade = num[2]
    print(f'Unidade: {num_unidade}')
    print(f'Dezena: {num_dezena}')
    print(f'Centena: {num_centena}')
    print(f'Milhar: {num_milhar}')

elif len(num) == 2:
    num_milhar = 0
    num_centena = 0
    num_dezena = num[0]
    num_unidade = num[1]
    print(f'Unidade: {num_unidade}')
    print(f'Dezena: {num_dezena}')
    print(f'Centena: {num_centena}')
    print(f'Milhar: {num_milhar}')

else:
    num_milhar = 0
    num_centena = 0
    num_dezena = 0
    num_unidade = num[0]
    print(f'Unidade: {num_unidade}')
    print(f'Dezena: {num_dezena}')
    print(f'Centena: {num_centena}')
    print(f'Milhar: {num_milhar}')
