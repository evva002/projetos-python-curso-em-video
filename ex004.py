texto = 'Desafio 004'
print('{:=^30}'.format(texto))

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(algo)))
print('É um número? {}'.format(algo.isnumeric()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print('Está em minúsculo? {}'.format(algo.islower()))

input("Pressione <enter> para encerrar!")