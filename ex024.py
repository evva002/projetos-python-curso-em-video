texto = 'Desafio 024'
print('{:=^30}'.format(texto))

nome_cidade = input('Digite o nome de uma cidade: ').strip()
print('O nome começa com Santo?')
print(nome_cidade[:5].upper() == 'SANTO')
