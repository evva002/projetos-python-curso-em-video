texto = 'Desafio 083'
print('{:=^30}'.format(texto))

expressao = str(input('Digite um expressão qualquer: '))
expressao_letras = list(expressao)
total_esq = 0
total_dir = 0
primeira_letra = False

if expressao_letras.count('(') == expressao_letras.count(')'):
    for c in expressao_letras:
        if c[0] == ')':
            print('Expressão inválida!')
            primeira_letra = True
            break
        elif total_dir > total_esq:
            print('Expressão inválida!')
            break
        elif c == '(':
            total_esq += 1 
        elif c == ')':
            total_dir += 1

    if total_esq == total_dir and primeira_letra == False:
        print('Expressão válida!')

else:
    print('Expressão inválida!')

input("Pressione <enter> para encerrar!")