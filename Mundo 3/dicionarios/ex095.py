texto = 'Desafio 095'
print('{:=^35}'.format(texto))

jogador = {}
jogadores = []
gol_formatado_lista = []

while True:
    gol_partida = []
    total_gol = 0
    print('=' * 35)
    jogador['nome'] = str(input('Digite o nome do jogador: ').upper())
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        gol = int(input(f'Quantos gols na {c + 1}ª partida? '))
        gol_partida.append(gol)
        total_gol += gol

    jogador['qtd_gol_partida'] = gol_partida[:]
    jogador['total_gol'] = total_gol
    jogadores.append(jogador.copy())

    print('=' * 35)
    escolha = str(input('Deseja continuar[S/N]? ').upper())
    print('=' * 35)
    if escolha == 'N':
        break

print(f'{'cod':<5}{'nome':<10}{'gols':<15}{'total':<5}')
for i, c in enumerate(jogadores):
    gol_formatado = str(jogadores[i]['qtd_gol_partida'])
    print(f'{i:<5}{jogadores[i]['nome']:<10}{gol_formatado:<15}{jogadores[i]['total_gol']:<5}')

while True:
    escolha = int(input('Mostrar dados de qual jogador[cod]? [999 para sair]: '))
    if escolha == 999:
        print('=' * 35)
        break
    elif escolha >= len(jogadores):
        print('=' * 35)
        print('Escolha incorreta, tente novamente!')
        print('=' * 35)
    else:
        gol_formatado = str(jogadores[escolha]['qtd_gol_partida'])
        gol_formatado_lista = (jogadores[escolha]['qtd_gol_partida'])
        print('=' * 35)
        print(f'{'nome':<10}{'gols':<15}{'total':<5}')
        print('=' * 35)
        print(f'{jogadores[escolha]['nome']:<10}{gol_formatado:<15}{jogadores[escolha]['total_gol']:<5}')
        print('=' * 35)
        print(f'---LEVANTAMENTO JOGADOR {jogadores[escolha]['nome']}---')
        print('=' * 35)
        for i, c in enumerate(gol_formatado_lista):
            print(f'No jogo {i + 1} fez {gol_formatado_lista[i]} gols')
            print('=' * 35)

input("Pressione <enter> para encerrar!")