texto = 'Desafio 059'
print('{:=^30}'.format(texto))

escolha = 0

while escolha != 5:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    escolha = int(input("""
[1] somar
[2] multiplicar
[3] maior                  
[4] novos números                   
[5] sair do programa: 
Selecione: """))
    if escolha == 1:
        soma = num1 + num2
        print(f'A soma dos números {num1:.2f} e {num2:.2f} é: {soma:.2f}')
        break
    elif escolha == 2:
        multiplicar = num1 * num2
        print(f'A multiplicação entre o número {num1:.2f} e o número {num2:.2f} é: {multiplicar:.2f}')
        break
    elif escolha == 3:
        if num1 > num2:
            print(f'O número {num1:.2f} é maior que o {num2:.2f}')
        else:
            print(f'O número {num2:.2f} é maior que o {num1:.2f}')
        break
    elif escolha == 4:
        print('-=' * 10)
        print('Selecione novos números.')
        print('-=' * 10)
    elif escolha == 5:
        print('Você selecionou "sair". Até mais!')
        break
    else:
        print('O valor digitado está incorreto, tente novamente.')

input("Pressione <enter> para encerrar!")