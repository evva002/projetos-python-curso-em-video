texto = 'Desafio 093'
print('{:=^30}'.format(texto))

jogador = {}
gol_partida = []
total_gol = 0
jogador['nome'] = str(input('Digite o nome do jogador: ').upper())
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(partidas):
    gol = int(input(f'Quantos gols na {c + 1}ª partida? '))
    gol_partida.append(gol)
    total_gol += gol

jogador['qtd_gol_partida'] = gol_partida[:]
jogador['total_gol'] = total_gol

print('=' * 30)
print(jogador)
print('=' * 30)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
for c in range(partidas):
    print(f'Na {c + 1}ª partida , fez {jogador['qtd_gol_partida'][c]} gols')

print('=' * 30)
print(f'{jogador['nome']} fez um total de {jogador["total_gol"]} gols.')
print('=' * 30)

input("Pressione <enter> para encerrar!")