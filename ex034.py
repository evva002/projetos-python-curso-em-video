texto = 'Desafio 034'
print('{:=^30}'.format(texto))

salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    print(f'O novo salário com acréscimo de 10% é: R${salario * 0.10 + salario}')
else:
    print(f'O novo salário com acréscimo de 15% é: R${salario * 0.15 + salario}')

input("Pressione <enter> para encerrar!")