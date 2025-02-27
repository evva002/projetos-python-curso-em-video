def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 097'
titulo(texto)

def escreva(mensagem):
    tamanho = len(mensagem) + 6
    print('=' * tamanho)
    print(f'   {mensagem}')
    print('=' * tamanho)

mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)

input("Pressione <enter> para encerrar!")