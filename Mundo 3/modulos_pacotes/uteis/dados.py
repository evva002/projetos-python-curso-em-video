from uteis import moeda

def verifiacao():
    print('=' * 30)
    valor = input('Digite o preço: R$')
    aumentar_porcentagem = input('Quantos % deseja aumentar: ')
    reduzir_porcentagem = input('Quantos % deseja reduzir: ')
    print('=' * 30)
    while True:
        try:
            aumentar_porcentagem = int(aumentar_porcentagem)
            reduzir_porcentagem = int(reduzir_porcentagem)
            if '.' in valor or ',' in valor:
                valor = float(valor.replace(',', '.'))
                return moeda.resumo(valor, aumentar_porcentagem, reduzir_porcentagem)
            else:
                valor = float(valor)
                return moeda.resumo(valor, aumentar_porcentagem, reduzir_porcentagem)
        except ValueError:
            print('Algum valor digitado não é um número válido! tente novamente.')
            