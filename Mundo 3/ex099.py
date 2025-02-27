from random import randint

def titulo(texto):
    print(f'{texto:=^30}')

texto = 'Desafio 099'
titulo(texto)

def maior(*valores):
    maior = max(valores)
    print(f'A lista gerada foi: {valores}')
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor da lista é {maior}')

numeros = []

for c in range (5):
    numeros.append(randint(1, 100))
    
maior(*numeros)

input("Pressione <enter> para encerrar!")