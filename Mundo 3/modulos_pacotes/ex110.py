import moeda

def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 110')

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

moeda.resumo(preco, aumentar_porcentagem, reduzir_porcentagem)

input("Pressione <enter> para encerrar!")