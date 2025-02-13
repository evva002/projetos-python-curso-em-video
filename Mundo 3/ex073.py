texto = 'Desafio 073'
print('{:=^30}'.format(texto))

print('=-' * 10)
print('BRASILEIRAO 2024')
print('=-' * 10)

classificacao = ('botafogo', 'palmeiras', 'flamengo', 'fortaleza', 'internacional', 'sao paulo', 'corinthians',
                 'bahia', 'cruzeiro', 'vasco', 'vitoria', 'atletico-mg', 'fluminense', 'gremio', 'juventude',
                 'bragantino', 'athletico-pr', 'criciuma', 'atletico-go', 'cuiaba')

print(classificacao)
print('=-' * 10)

print('Os primeiros 5 colocados:')
# print(f'Os primeiros 5 colocados são: {classificacao[0:5]}')
for time in range (0, 5):
    print(f'{time + 1}º{classificacao[time].upper()}')

print('=-' * 10)
print('Os últimos 4 colocados:')
# print(f'\nOs últimos 4 colocados: {classificacao[16:20]}')
for time in range (16, 20):
    print(f'{time + 1}º{classificacao[time].upper()}')

print('=-' * 10)
print(f'Times em ordem alfábetica: {sorted(classificacao)}')

print('=-' * 10)
pos_tabela = 0
time = str(input('Digite um time para saber sua posição na tabela: ')).lower().strip()

if time in classificacao:
    pos_tabela = classificacao.index(time) + 1
    print(f'O {time} está classificado na posição {pos_tabela}º')
        
else:
    print(f'O time {time} não está na tabela')
        
print('=-' * 10)

input("Pressione <enter> para encerrar!")