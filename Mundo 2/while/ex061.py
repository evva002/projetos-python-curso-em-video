texto = 'Desafio 061'
print('{:=^30}'.format(texto))

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
maximo = termo

while c < maximo:
    print(f'Termo nº {c}: {termo}')
    termo += razao
    c += 1

input("Pressione <enter> para encerrar!")   