texto = 'Desafio 055'
print('{:=^30}'.format(texto))

maior_peso = 0.0
menor_peso = 0.0

for c in range(1, 6):
    peso = float(input('Digite o seu peso(0.00): '))
    if menor_peso == 0 and maior_peso == 0:
        menor_peso = peso
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
        
print(f'O maior peso foi {maior_peso:.2f}KG e o menor peso foi {menor_peso:.2f}KG')