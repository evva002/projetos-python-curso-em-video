texto = 'Desafio 031'
print('{:=^30}'.format(texto))

distancia_viagem = float(input('Digite a distância da viagem: '))
if distancia_viagem < 200:
    print(f""""Valor por cada km percorrido é R$0,50 centavos.
O valor total da viagem foi de: R${distancia_viagem * 0.50}""")
else:
    print(f""""Valor por cada km percorrido é R$0,45 centavos.
O valor total da viagem foi de: R${distancia_viagem * 0.45}""")