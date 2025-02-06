texto = 'Desafio 040'
print('{:=^30}'.format(texto))

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Aprovado! sua média foi {media}')
elif media >= 5 and media < 7:
    print(f'Recuperação! sua média foi {media}')
else:
    print(f'Reprovado! sua média foi {media}')

input("Pressione <enter> para encerrar!")