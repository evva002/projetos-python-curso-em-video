texto = 'Desafio 071'
print('{:=^30}'.format(texto))

print('-=' * 10)
print('BANCO DO CARLAO')
print('-=' * 10)

valor_saque = int(input('Digite o valor do saque: R$'))
resto = 0
total_notas_50 = 0
total_notas_20 = 0
total_notas_10 = 0
total_notas_1 = 0

while valor_saque > 0:
    if valor_saque >= 50:
        total_notas_50 = valor_saque // 50 
        valor_saque -= total_notas_50 * 50
    if valor_saque >= 20:
        total_notas_20 = valor_saque // 20
        valor_saque -= total_notas_20 * 20
    if valor_saque >= 10:
        total_notas_10 = valor_saque // 10
        valor_saque -= total_notas_10 * 10
    if valor_saque >= 1:
        total_notas_1 = valor_saque // 1
        valor_saque -= total_notas_1 * 1

print('-=' * 10)
print(f'Notas de R$50: {total_notas_50}')
print(f'Notas de R$20: {total_notas_20}')
print(f'Notas de R$10: {total_notas_10}')
print(f'Notas de R$1: {total_notas_1}')
print('-=' * 10)
print('Volte sempre, até mais!')
print('-=' * 10)

input("Pressione <enter> para encerrar!")