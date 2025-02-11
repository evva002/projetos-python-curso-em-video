from time import sleep

texto = 'Desafio 046'
print('{:=^30}'.format(texto))

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Fim!')

input("Pressione <enter> para encerrar!")