import math

texto = 'Desafio 017'
print('{:=^30}'.format(texto))

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa é: {hipotenusa:.2f}')

input("Pressione <enter> para encerrar!")