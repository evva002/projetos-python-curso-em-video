texto = 'Desafio 067'
print('{:=^30}'.format(texto))

while True:
    print('-=' * 10)
    num = int(input('Digite um número para mostrar sua tabuada: '))
    print('-=' * 10)
    if num < 0:
        break
    else:
        for c in range(1, 11):
            multiplicacao = c * num
            print(f'{num} X {c} = {multiplicacao}') 
            
input("Pressione <enter> para encerrar!")          