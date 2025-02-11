texto = 'Desafio 044'
print('{:=^30}'.format(texto))

valor = float(input('Digite o valor do produto: R$'))
print("""Métodos de pagamento:
[1] - À vista no dinheiro: 10% de desconto. Digite 1
[2] - À vista no cartão de crédito: 5% de desconto. Digite 2
[3] - Em até 2X no cartão de crédito: preço normal. Digite 3
[4] - em 3X ou mais no cartão de crédito: 20% de juros. Digite 4""")
pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    print(f'O valor final ficou: R${valor * 0.9:.2f}')
elif pagamento == 2:
    print(f'O valor final ficou: R${valor * 0.95:.2f}')
elif pagamento == 3:
    valor_parcelado = valor / 2
    print(f'O valor final ficou: R${valor:.2f}')
    print(f'O valor parcelado ficou: 2 X R${valor_parcelado:.2f}')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_juros = valor * 1.2
    print(f'O valor final ficou: R${valor_juros:.2f} com juros.')
    print(f'Sua compra parcelada irá ficar {parcelas} X {valor_juros / parcelas:.2f}')
else:
    print('Opção incorreta. Execute o código novamente.')

input("Pressione <enter> para encerrar!")