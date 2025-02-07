texto = 'Desafio 053'
print('{:=^30}'.format(texto))

frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print(f'A frase {frase} é um palíndromo, pois o seu contrário é {frase_invertida}.')
else:
    print(f'A frase {frase} não é um palíndromo, pois o seu contrário é {frase_invertida}.')

input("Pressione <enter> para encerrar!")