texto = 'Desafio 009'
print('{:=^30}'.format(texto))

num = int(input('Digite um número para mostrar sua tabuada: '))
contador = (1)
for contador in range(1, 11):
    print('{} X {} = {}'.format(num, contador, num * contador))
    contador += 1

input("Pressione <enter> para encerrar!")   