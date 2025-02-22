texto = 'Desafio 076'
print('{:=^30}'.format(texto))

lista_de_precos = ('Monitor', 650, 
                   'Mouse', 49.90, 
                   'Teclado', 199.90, 
                   'Processador', 299.90,
                   'Gabinete', 149.90)
titulo = 'LISTA DE PREÇOS'
print('-' * 30)
print(f'{titulo:^30}')
print('-' * 30)
for i, c in enumerate(lista_de_precos):
    if i % 2 == 0:
        print(f'{c:.<20}', end="")
    else:
        print(f'R${c:>8.2f}')

print('-' * 30)

input("Pressione <enter> para encerrar!")