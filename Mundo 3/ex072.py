texto = 'Desafio 072'
print('{:=^30}'.format(texto))

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte' )

num = int(input('Digite um número entre 0 e 20: '))

while True:
    if num > 20 or num < 0:
        num = int(input('Número fora da lista. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numeros[num]}')    
        break

input("Pressione <enter> para encerrar!")