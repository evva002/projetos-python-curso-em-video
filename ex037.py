texto = 'Desafio 037'
print('{:=^30}'.format(texto))

num = int(input('Digite um número para conversão: '))
escolha = int(input("""Escolha: 
1 para binário
2 para octal 
3 para hexadecimal 
>>>: """))
num_imutavel = num
resultado_binario = ''
resultado_octal = ''
resultado_hexadecimal = ''
hexadecimal_numeros = '0123456789ABCDEF'

#calculo para conversão do número em binário 
if escolha == 1:      
        while num >= 0: 
                if num > 0:
                        resto = num % 2
                        resultado_binario = str(resto) + resultado_binario
                        num //= 2
                else:
                        break
        print(f'O número {num_imutavel} em binário é {resultado_binario}')

#calculo para conversão do número em octal
elif escolha == 2:      
        while num >= 0: 
                if num > 0:
                        resto = num % 8
                        resultado_octal = str(resto) + resultado_octal
                        num //= 8
                else:
                        break
        print(f'O número {num_imutavel} em octal é {resultado_octal}')

#calculo para conversão do número em hexadecimal
elif escolha == 3:      
        while num >= 0: 
                if num > 0:
                        resto = num % 16
                        resultado_hexadecimal = hexadecimal_numeros[resto] + resultado_hexadecimal
                        num //= 16
                else:
                        break
        print(f'O número {num_imutavel} em hexadecimal é {resultado_hexadecimal}')
else:
        print(f'O número {escolha} não está nas opcões, execute o código novamente!')

input("Pressione <enter> para encerrar!")


