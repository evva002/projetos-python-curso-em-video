texto = 'Desafio 030'
print('{:=^30}'.format(texto))

ano = int(input('Digite um ano qualquer para descobrir se ele é bissexto: '))
ano_lista = list(map(int, str(ano)))

print(ano % 4)
print(ano % 400)
print(ano_lista[-2:])

if ano_lista[-2:] == [0, 0]:
    if ano % 4 == 0 and ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto')
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto')