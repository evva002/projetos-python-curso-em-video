texto = 'Desafio 027'
nome = input('Digite seu nome completo: ')
nome_dividido = nome.split()
print(f'O seu primeiro nome é: {nome_dividido[0]}')
print(f'O seu segundo nome é: {nome_dividido[len(nome_dividido) - 1]}')