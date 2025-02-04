texto = 'Desafio 022'
print('{:=^30}'.format(texto))

nome = input('Digite seu nome completo: ')
print('Nome upper: nome.upper()')
print('Nome lower: nome.lower()')
nome_sem_espacos = nome.replace(' ', '')
print(f'O nome sem espaços fica {nome_sem_espacos} e possui {len(nome_sem_espacos)} caracteres.')
nome_dividido = nome.split()
print(f'O primeiro nome é {nome_dividido[0]} e possui {len(nome_dividido[0])} caracteres')
