texto = 'Desafio 010'
print('{:=^30}'.format(texto))
carteira = float(input('Digite o valor que você possui em reais: '))
print('Você pode comprar ${:.2f} dólares com R${:.2f} reais.'.format(carteira / 5.86, carteira))