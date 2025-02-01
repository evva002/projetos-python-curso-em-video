texto = 'Desafio 015'
print('{:=^30}'.format(texto))
quantidade_dia = int(input('Digite a quantidade de dias usando o carro: '))
quantidade_km = float(input('Digite a quantidade de quilômetros percorridos com o carro: '))
valor_aluguel = (quantidade_dia * 60) + (quantidade_km * 0.15)
print(f'O valor total o aluguel é: R${valor_aluguel}')