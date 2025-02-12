texto = 'Desafio 069'
print('{:=^30}'.format(texto))

sair = False
mulheres_20 = 0
pessoas_18 = 0
homens = 0

while not sair:
    print('-=' * 10)
    print('Olá, digite o sexo e a idade da pessoa: ')
    print('-=' * 10)
    sexo = str(input('Digite seu sexo (M/F): ')).upper()
    idade = int(input('Digite sua idade: '))

    if idade >= 18:
        pessoas_18 += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    if sexo == 'M':
        homens += 1

    escolha = str(input('Deseja continuar? [S / N] ')).upper().strip()

    if escolha == 'N':
        sair = True

print('-=' * 10)
print(f'A quantidade de pessoas que tem mais que 18 anos é: {pessoas_18}')
print(f'A quantidade de homens cadastrados foi: {homens}')
print(f'A quantidade de mulheres com menos de 20 anos foi: {mulheres_20}')
print('-=' * 10)

input("Pressione <enter> para encerrar!")