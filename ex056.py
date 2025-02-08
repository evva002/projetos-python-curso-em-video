texto = 'Desafio 056'
print('{:=^30}'.format(texto))

media_idade = 0.0
mulheres_20 = 0
homem_mais_velho = 'Não consta nenhum homem na pesquisa'
idade_mais_velho_m = 0

for c in range(1, 5):
    print(f'Olá, você é a pessoa número {c}º')
    nome = str(input(f'Digite seu nome: ')).upper()
    sexo = str(input('Digite seu sexo (M/F): ')).upper()
    idade = int(input('Digite sua idade: '))

    media_idade += idade

    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    elif sexo == 'M' and idade > idade_mais_velho_m:
        homem_mais_velho = nome
        idade_mais_velho_m = idade

media_idade = media_idade / 4

print(f'a média de idade do grupo foi de: {media_idade:.2f} anos')
print(f'O nome do homem mais velho é: {homem_mais_velho}')
print(f'O número de mulheres com menos de 20 anos foi: {mulheres_20}')