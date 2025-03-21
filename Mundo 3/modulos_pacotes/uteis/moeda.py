def metade(valor, converter=False):
    valor = valor / 2
    if converter == True:
        return converterMoeda(valor)
    else:
        valor = round(valor, 2)
        return valor

def dobro(valor, converter=False):
    valor = valor * 2
    if converter == True:
        return converterMoeda(valor)
    else:
        valor = round(valor, 2)
        return valor

def aumentar(valor, porcentagem, converter=False):
    valor = valor * (1 + (porcentagem / 100))
    if converter == True:
        return converterMoeda(valor)
    else:
        valor = round(valor, 2)
        return valor

def reduzir(valor, porcentagem, converter=False):
    porcentagem = abs(porcentagem)
    valor = valor * (1 - (porcentagem / 100))
    if converter == True:
        return converterMoeda(valor)
    else:
        valor = round(valor, 2)
        return valor
    
def converterMoeda(valor, formatoMoeda='R$'):
    return f'{formatoMoeda}{valor:.2f}'.replace('.', ',')

def resumo(valor, aumentar_porcentegem, reduzir_porcentagem):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'{'Preço analisado:':<18}{converterMoeda(valor):>12}')
    print(f'{'Metade do preço:':<18}{metade(valor, True):>12}')
    print(f'{'Dobro do preço:':<18}{dobro(valor, True):>12}')
    print(f'{aumentar_porcentegem:<3}{'% de aumento':<17}{aumentar(valor, aumentar_porcentegem, True):>10}')
    print(f'{reduzir_porcentagem:<3}{'% de redução:':<17}{reduzir(valor, reduzir_porcentagem, True):>10}')
    print('-' * 30)