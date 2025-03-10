texto = 'Desafio 077'
print('{:=^30}'.format(texto))

palavras = ('maca', 'uva', 'mesa', 'cama', 'banana', 'ventilador', 
            'computador','jogos', 'trabalho')
vogais = 'aeiou'

for c in palavras:
    print('\n')
    palavra_fatiada = tuple(c.upper())
    print(f'A palavra {c} possui as vogais:', end=" ")
    for letra in palavra_fatiada:
        if letra in vogais.upper():
            print(letra.lower(), end=" ")

print('\n')
input("Pressione <enter> para encerrar!")