def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 096'
titulo(texto)

def area(a, b):
    c = a * b
    return(c)

def linha():
    print('=' * 30)

def titulo(texto):
    print(f'{texto:^30}')

linha()
titulo('CALCULADORA DE AREA')
linha()
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
print(f'Para o comprimento {comprimento:.2f}m e largura {largura:.2f}m temos a área de {area(largura, comprimento):.2f}m²')

input("Pressione <enter> para encerrar!")