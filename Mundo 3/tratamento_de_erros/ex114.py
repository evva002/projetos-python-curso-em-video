def titulo(texto):
    print(f'{texto:=^30}')

titulo('Desafio 114')

def testaSite():
    import requests
    site = 'https://google.com.br'
    try:
        response = requests.get(site, timeout=5)
        if response.status_code == 200:
            print(f'O site >>> {site} <<< está acessível no momento!')

    except requests.RequestException as erro:
        print(f'Erro inesperado: {erro}')

testaSite()

print('='*30)
input("Pressione <enter> para encerrar!")