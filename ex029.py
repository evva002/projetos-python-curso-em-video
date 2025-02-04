texto = 'Desafio 029'
print('{:=^30}'.format(texto))

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade >= 80:
    valor_multa = (velocidade - 80) * 7
    print(f"""Você estava acima da velocidade máxima permititda da via que é de 80km/h, 
o valor da sua multa é R${valor_multa}""")
else:
    print('Você estava dentro da vocidade permitida de 80km/h')
