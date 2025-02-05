from datetime import date

texto = 'Desafio 039'
print('{:=^30}'.format(texto))

data_hoje = date.today()

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = data_hoje.year - ano_nascimento
if idade < 18:
    print(f'Você ainda possui {idade} anos, não precisa se alistar ainda.')
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'O seu ano de alistamento será: {ano_nascimento + 18}.')
elif idade == 18:
    print(f'Você possui {idade} anos, deve fazer o alistamento neste ano ainda.')
else:
    print(f'Você possui {idade} anos')
    print(f'Seu alistamento foi no ano de {ano_nascimento + 18}.')
    print(f'Seu alistamento foi há {idade - 18} anos.')
