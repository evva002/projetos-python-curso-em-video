import math
texto = 'Desafio 018'
print('{:=^30}'.format(texto))
angulo_graus = float(input('Digite o ângulo desejado: '))
seno_angulo = math.sin(math.radians(angulo_graus))
coseno_angulo = math.cos(math.radians(angulo_graus))
tangente_angulo = math.tan(math.radians(angulo_graus))
print(f'Para o ângulo {angulo_graus}°, temos o seno de {seno_angulo:.2f}, coseno {coseno_angulo:.2f} e tangente {tangente_angulo:.2f}.')