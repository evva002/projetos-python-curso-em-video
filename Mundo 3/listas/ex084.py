texto = 'Desafio 084'
print('{:=^30}'.format(texto))

pessoa = []
pessoas = []
maior_peso = []
menor_peso = []

while True:
    print('=' * 30)
    escolha = str(input('Deseja cadastrar uma pessoa [S/N]? ')).upper()
    print('=' * 30)

    if escolha == 'N':
        maior_peso = max(pessoas, key=lambda x: x[1])[1]
        menor_peso = min(pessoas, key=lambda x: x[1])[1]
        break
    elif escolha == 'S':
        pessoa.append(str(input('Digite o NOME da pessoa: ').upper()))
        pessoa.append(float(input('Digite o PESO da pessoa: ')))
        pessoas.append(pessoa[:])
        pessoa.clear()
    else:
        print('Escolha incorreta, tente novamente!')

print(f'Você cadastrou o total de {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi de {maior_peso:.2f}KG. Nomes: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}...', end='')
print(f'\nO menor peso cadastrado foi de {menor_peso:.2f}KG. Nomes: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}...', end='')

print()

input("Pressione <enter> para encerrar!")