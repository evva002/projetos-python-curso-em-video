def menuPrincipal():
    import relatorio
    import cadastrar
    import time
    while True:   
        print('='*30)
        print(f'{'MENU PRINCIPAL':^30}')
        print('='*30)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('='*30)
        try:
            escolha = int(input('Sua opcão: '))
            if escolha == 1:
                relatorio.verPessoa()
            elif escolha == 2:
                cadastrar.cadastrarPessoa()
            elif escolha == 3:
                print('='*30)
                print('Saindo...')
                time.sleep(2)
                print('Até logo!')
                print('='*30)
                break
            else:
                print('Número fora do range, tente novamente!')
        except (ValueError):
            print('Escolha incorreta, tente novamente!')