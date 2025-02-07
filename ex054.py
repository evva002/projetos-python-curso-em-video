from datetime import date

texto = 'Desafio 053'
print('{:=^30}'.format(texto))

data_hoje = date.today().year

maior_idade = 0
menor_idade = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if data_hoje - ano >= 18:
        maior_idade += 1 
    else:
        menor_idade += 1

print(f'Ao todo foram {maior_idade} maiores de idade e {menor_idade} menores de idade.')

input("Pressione <enter> para encerrar!")