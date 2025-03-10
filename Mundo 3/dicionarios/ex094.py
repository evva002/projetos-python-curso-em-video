texto = 'Desafio 094'
print('{:=^30}'.format(texto))

pessoa = {}
pessoas = []
media_idade = 0.0

while True:
    print('=' * 30)
    pessoa['nome'] = str(input('Nome: ').upper())
    pessoa['sexo'] = str(input('Sexo[M/F]: ').upper())
    pessoa['idade'] = int(input('Idade: '))
    media_idade += pessoa['idade']
    pessoas.append(pessoa.copy())
    print('=' * 30)
    escolha = str(input('Deseja continuar[S/N]? ').upper())
    print('=' * 30)

    if escolha == 'N':
        break

media_idade = media_idade / len(pessoas)

print('=' * 30)
print(f'O grupo possui {len(pessoas)} pessoas')
print('As mulheres cadastradas foram: ', end='')

for c in range(len(pessoas)):
    if pessoas[c]['sexo']== 'F':
        print(f'{pessoas[c]['nome']}', end=' ')
print()

print(f'A média de idade é {media_idade:.2f} anos')
print('Lista de pessoas acima da média: ')

for c in range(len(pessoas)):
    if pessoas[c]['idade'] > media_idade:
        print(f'{pessoas[c]}')
print('=' * 30)

input("Pressione <enter> para encerrar!")