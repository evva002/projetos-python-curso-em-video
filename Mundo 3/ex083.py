texto = 'Desafio 083'
print('{:=^30}'.format(texto))

expressao = str(input('Digite um expressão qualquer: '))
expressao_letras = list(expressao)

if expressao_letras.count('(') == expressao_letras.count(')'):
    print('A expressão é válida!')
else:
    print('A expressão inválida!')

input("Pressione <enter> para encerrar!")