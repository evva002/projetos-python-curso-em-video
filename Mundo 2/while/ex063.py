texto = 'Desafio 063'
print('{:=^30}'.format(texto))

num = int(input('Digite até qual elemento você deseja ver na sequência de Fibonacci: '))
c = 0
termo1 = 0
termo2 = 1

while c <= num:
    print(termo1)
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    c += 1
    
input("Pressione <enter> para encerrar!")