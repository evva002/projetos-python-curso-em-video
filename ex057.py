texto = 'Desafio 057'
print('{:=^30}'.format(texto))

sexo = ''
sexo = str(input('Digite seu sexo (M/F): ')).upper()[0]
print(sexo)

while sexo not in ('M', 'F'):
    print('Valor incorreto, favor digitar novamente.')
    sexo = str(input('Digite seu sexo (M/F): ')).upper()[0]

input("Pressione <enter> para encerrar!")