texto = 'Desafio 062'
print('{:=^30}'.format(texto))

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
maximo = termo

while c <= maximo:
    print(f'Termo nº {c}: {termo}')
    termo += razao
    c += 1
    
novos_termos = int(input('Você deseja adicionar mais termos(Digite [0] para sair)? se sim, quantos? '))

if novos_termos == 0:
    print('Adeus!')
else:
    while c <= (maximo + novos_termos):
        print(f'Termo nº {c}: {termo}')
        termo += razao
        c += 1

input("Pressione <enter> para encerrar!")   