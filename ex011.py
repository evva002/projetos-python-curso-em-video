texto = 'Desafio 011'
print('{:=^30}'.format(texto))
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'{largura:.2f} X {altura:.2f} = {largura:.2f * altura:.2f}m²')
print(f'A quantidade de tinta necessária para pintar essa parede é {(largura * altura) / 2} litros')