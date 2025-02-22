texto = 'Desafio 075'
print('{:=^30}'.format(texto))

qtd_nove = 0
posicao_tres = -1
numeros = tuple(int(input('Digite um número: ')) for c in range(4))

print(f'Tupla digitada:{numeros}')
  
for i, c in enumerate(numeros):
    if c == 3:
        posicao_tres = i + 1
    if c == 9:
        qtd_nove += 1
    if c % 2 == 0:
        print(f'O número {c} é par')
        
if posicao_tres >= 0:
    print(f'O número "três" foi encontrado na posição: {posicao_tres}')
else:
    print('Não foi encontrado um número três na tupla')

print(f'A quantidade de números "nove" digitados foram: {qtd_nove}')

input("Pressione <enter> para encerrar!")