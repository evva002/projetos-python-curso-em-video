def cadastrarPessoa():
    try:
        print('-' * 30)
        print(f'{'CADASTRAR':^30}')
        print('-' * 30)
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
    except (ValueError, TypeError):
        print('Valor digitado incorreto! por favor digite um número inteiro.')
    except Exception as erro:
        print(f'Erro: {erro.__class__}')
    
    with open(r'C:\Users\carlo\OneDrive\Documentos\codigos\projetos-python-curso-em-video\Mundo 3\tratamento_de_erros\exercicio115-116-117\relatorio.txt', 'a') as relatorio:
        relatorio.write(f'{nome:<20}{idade:>5}{'anos':>5}\n')