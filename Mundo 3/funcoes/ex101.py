def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 101'
titulo(texto)

def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.today()
    idade = ano_atual.year - ano_nascimento
    if idade >= 18:
        print(f'Você possui {idade} anos: ', end='')
        situação = 'VOTO OBRIGATÓRIO'
        return situação
    elif idade >= 65 or 18 > idade >= 16:
        print(f'Você possui {idade} anos: ', end='')
        situação = 'VOTO OPCIONAL'
        return situação
    else:
        print(f'Você possui {idade} anos: ', end='')
        situação = 'NÃO VOTA'
        return situação
    
ano_nascimento = int(input('Em que ano você nasceu? '))
situacao = voto(ano_nascimento)
print(situacao)
print('=' * 30)

input("Pressione <enter> para encerrar!")