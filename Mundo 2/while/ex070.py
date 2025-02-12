texto = 'Desafio 070'
print('{:=^30}'.format(texto))

sair = False
qtd_mais_1000 = 0
total_gasto = 0
nome_mais_barato = ''
valor_mais_barato = 0
escolha = ''

while not sair:
    print('-=' * 10)
    print('LOJA DO CARLAO')
    print('-=' * 10)

    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = float(input('Digite o valor do produto: R$'))

    total_gasto += valor_produto
    if valor_mais_barato == 0:
        valor_mais_barato = valor_produto
        nome_mais_barato = nome_produto

    elif valor_produto < valor_mais_barato:
        valor_mais_barato = valor_produto
        nome_mais_barato = nome_produto

    elif valor_produto >= 1000:
        qtd_mais_1000 += 1

    escolha = (str(input('Deseja continuar? [S / N]'))).upper().strip()
    if escolha == 'N':
        sair = True

print('-=' * 10)
print(f'RESUMO DA COMPRA')
print('-=' * 10)
print(f'O total gasto na compra foi: R${total_gasto:.2f}')
print(f'A quantidade de produtos que custa mais que R$1000 foi: {qtd_mais_1000}')
print(f'O nome do produto mais barato foi: {nome_mais_barato} e seu valor foi de R${valor_mais_barato:.2f}')
print('-=' * 10)

input("Pressione <enter> para encerrar!")