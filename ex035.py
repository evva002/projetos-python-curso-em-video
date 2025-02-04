texto = 'Desafio 034'
print('{:=^30}'.format(texto))

triangulo1 = float(input('Digite o valor do primeiro triângulo: '))
triangulo2 = float(input('Digite o valor do segundo triângulo: '))
triangulo3 = float(input('Digite o do terceiro triângulo: '))

if triangulo1 + triangulo2 > triangulo3 and triangulo1 + triangulo3 > triangulo2 and triangulo2 + triangulo3 > triangulo1:
    print('Os valores das retas podem formar um triângulo!')
else:
    print('Os valores das retas >>> NÃO <<< podem formar um triângulo!')