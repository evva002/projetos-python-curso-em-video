from uteis import moeda

# Contém os exercícios 107, 108 e 109

def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 107, 108 e 109')

while True:
    print('=' * 30)
    preco = input('Digite o preço: R$')
    aumentar_porcentagem = input('Quantos % deseja aumentar: ')
    reduzir_porcentagem = input('Quantos % deseja reduzir: ')
    print('=' * 30)
    try:
        aumentar_porcentagem = int(aumentar_porcentagem)
        reduzir_porcentagem = int(reduzir_porcentagem)
        if '.' in preco or ',' in preco:
            preco = float(preco.replace(',', '.'))
            break
        else:
            preco = float(preco)
            break
    except ValueError:
        print('Algum valor digitado não é um número válido! tente novamente.')

print('=' * 30)
print(f'A metade de {moeda.converterMoeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.converterMoeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentado {aumentar_porcentagem}%, temos {moeda.aumentar(preco, aumentar_porcentagem, True)}')
print(f'Reduzindo {reduzir_porcentagem}%, temos {moeda.reduzir(preco, reduzir_porcentagem, True)}')
print('=' * 30)

input("Pressione <enter> para encerrar!")