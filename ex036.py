texto = 'Desafio 036'
print('{:=^30}'.format(texto))

valor_casa = float(input('Digite o valor da casa desejada: R$'))
salario = float(input('Digite o seu sálario mensal: R$'))
anos = int(input('Digite em quantos anos você deseja parcelar a casa: '))
salario_30 = salario * 0.30
anos_meses = anos * 12
valor_parcela = valor_casa / anos_meses

if (salario_30) > (valor_parcela):
    print(f'30% do salário: R${salario_30:.2f}')
    print(f'Meses de financiamento: {anos_meses}')
    print(f'Valor da parcela: R${valor_parcela:.2f}')
    print('Parabéns, seu empréstimo foi aprovado!')
else: 
    print(f'30% do salário: R${salario_30:.2f}')
    print(f'Meses de financiamento: {anos_meses}')
    print(f'Valor da parcela: R${valor_parcela:.2f}')
    print("""Infelizmente o seu empréstimo não foi aprovado, 
pois o valor da parcela ultrapassou 30% do seu salário""")

input("Pressione <enter> para encerrar!")