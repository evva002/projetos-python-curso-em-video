texto = 'Desafio 048'
print('{:=^30}'.format(texto))

soma_impares = 0
soma_unidade = 0

for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma_impares += c
        soma_unidade += 1
                        
print(f'A soma de todos os {soma_unidade} valores solitados é de: {soma_impares}')

input("Pressione <enter> para encerrar!")