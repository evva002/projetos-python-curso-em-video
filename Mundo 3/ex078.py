texto = 'Desafio 078'
print('{:=^30}'.format(texto))

numeros = []

for c in range(5):
    numeros.append(int(input(f'Digite o {c + 1}º número: ')))

print(f'A lista criada foi: {numeros}')
print(f'O maior número digite é {max(numeros)} e sua posição é a {numeros.index(max(numeros)) + 1}ª')
print(f'O menor número digite é {min(numeros)} e sua posição é a {numeros.index(min(numeros)) + 1}ª')

input("Pressione <enter> para encerrar!")