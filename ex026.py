texto = 'Desafio 026'
frase = input('Digite uma palavra ou frase: ').upper().strip()
print(f'A palavra ou frase possui {frase.count('A')} As.')
print(f'A primeira ocorrência de A está na posição: {frase.find('A')}')
print(f'A última ocorrência de A está na posição: {frase.rfind('A')}')