from random import randint
from time import sleep

texto = 'Desafio 091'
print('{:=^30}'.format(texto))

jogos = [{'jogador': 1, 'dado': 0}, 
        {'jogador': 2, 'dado': 0}, 
        {'jogador': 3, 'dado': 0}, 
        {'jogador': 4, 'dado': 0}]

print('=' * 30)
print(f'{'=' * 8}{'JOGO DE DADOS':^10}{'=' * 9}')
print('=' * 30)

for c in range(4):
    jogos[c]['dado'] = randint(1,6)
    sleep(1)
    print(f'O jogador {jogos[c]['jogador']} tirou {jogos[c]['dado']}')

jogo_ordenado = sorted(jogos, key=lambda jogo: jogo['dado'], reverse=True)

sleep(1)
print('=' * 30)
print('RANKING DOS JOGADORES')
print('=' * 30)

for c in range(4):
    sleep(1)
    print(f'{c + 1}º lugar: jogador {jogo_ordenado[c]['jogador']} com {jogo_ordenado[c]['dado']}')

print('=' * 30)

input("Pressione <enter> para encerrar!")