def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 105')

def notas_gerais(*notas, situacao=False):
    notas_lista = []
    geral_dict = {}
    soma_nota = 0
    for nota in notas:
        notas_lista.append(nota)
        soma_nota += nota
    
    geral_dict['maior nota'] = max(notas_lista)
    geral_dict['menor nota'] = min(notas_lista)
    geral_dict['media'] = soma_nota / len(notas_lista)

    if situacao == True:
        if geral_dict['media'] >= 7:
            geral_dict['situacao'] = 'BOA'
        elif geral_dict['media'] >= 5 and geral_dict['media'] < 7:
            geral_dict['situacao'] = 'RAZOAVEL'
        else:
            geral_dict['situacao'] = 'RUIM'
        print(f'Lista de notas passadas: {notas_lista}')
        print(geral_dict)
    else:
        print(f'Lista de notas passadas: {notas_lista}')
        print(geral_dict)

notas_gerais(5, 3, 2, 6, situacao=True)

input("Pressione <enter> para encerrar!")