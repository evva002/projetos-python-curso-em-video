texto = 'Desafio 035'
print('{:=^30}'.format(texto))

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Os valores das retas >>> PODEM FORMAR <<< um triângulo!')
else:
    print('Os valores das retas >>> NÃO PODEM <<< formar um triângulo!')

input("Pressione <enter> para encerrar!")