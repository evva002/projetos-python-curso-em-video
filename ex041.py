from datetime import date

texto = 'Desafio 041'
print('{:=^30}'.format(texto))

data_hoje = date.today()

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = data_hoje.year - ano

if idade < 9:
    print(f'O atleta possui {idade} anos.')
    print('Classificação: Mirim')
elif idade < 14:
    print(f'O atleta possui {idade} anos.')
    print('Classificação: Infantil')
elif idade < 19:
    print(f'O atleta possui {idade} anos.')
    print('Classificação: Junior')
elif idade <= 20:
    print(f'O atleta possui {idade} anos.')
    print('Classificação: Sênior')
else:
    print(f'O atleta possui {idade} anos.')
    print('Classificação: Master')

input("Pressione <enter> para encerrar!")   