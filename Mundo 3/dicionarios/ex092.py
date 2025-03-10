from datetime import datetime

texto = 'Desafio 092'
print('{:=^30}'.format(texto))

data_hoje = datetime.today()
dados = {}

dados['nome'] = str(input('Digite seu nome: ').upper())
dados['ano_nascimento'] = int(input('Digite seu ano de nascimento: '))
dados['carteira_trabalho'] = int(input('Digite o número da carteira de trabalho [digite 0 caso não tenha]: '))
dados['idade'] = data_hoje.year - dados['ano_nascimento']

if dados['carteira_trabalho'] != 0:
    dados['ano_contratacao'] = int(input('Digite o ano que você começou a trabalhar: '))
    dados['salario'] = float(input('Digite o sálario: R$'))
    dados['aposentadoria'] = (dados['ano_contratacao'] + 35) - dados['ano_nascimento']
    print('=' * 30)
    print(f'{'CARTEIRA DE TRABALHO':^30}')
    print('=' * 30)
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados['idade']}')
    print(f'Ano de nascimento: {dados["ano_nascimento"]}')
    print(f'N° carteira de trabalho: {dados['carteira_trabalho']}')
    print(f'Ano que começou a trabalhar: {dados['ano_contratacao']}')
    print(f'Salário: R${dados['salario']:.2f}')
    print(f'Irá se aposentar com {dados['aposentadoria']} anos no ano de {dados['ano_contratacao'] + 35}')
    print('=' * 30)
else:
    print('=' * 30)
    print(f'{'CADASTRO':^30}')
    print('=' * 30)
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {dados['idade']}')
    print(f'Ano de nascimento: {dados["ano_nascimento"]}')
    print(f'N° carteira de trabalho: {dados['carteira_trabalho']}')
    print('=' * 30)

input("Pressione <enter> para encerrar!")