def verPessoa():
    try:
        with open(r'C:\Users\carlo\OneDrive\Documentos\codigos\projetos-python-curso-em-video\Mundo 3\tratamento_de_erros\exercicio115-116-117\relatorio.txt', 'r') as relatorio:
            conteudo = relatorio.read()
            print('-' * 30)
            print(f'{'RELATORIO':^30}')
            print('-' * 30)
            print(conteudo)
            print('-' * 30)
    except Exception as erro:
        print(f'Erro: {erro.__class__}')