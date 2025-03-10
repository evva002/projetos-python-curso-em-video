def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 103')

def ficha(nome_jogador='<desconhecido>', gols=0):
    if len(nome_jogador) == 0:
        nome_jogador='<desconhecido>'
    print(f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato.')

nome_jogador = str(input('Digite o nome do jogador: ')).strip()
gols = input('Digite a quantidade de gols no campeonato: ')
gols = int(gols) if gols.isdigit() else 0

ficha(nome_jogador, gols)

input("Pressione <enter> para encerrar!")