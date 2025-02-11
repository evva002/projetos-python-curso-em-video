texto = 'Desafio 051'
print('{:=^30}'.format(texto))

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(1, 11):
    print(f'Termo nº {c}: {termo}')
    termo += razao

input("Pressione <enter> para encerrar!")   