texto = 'Desafio 014'
print('{:=^30}'.format(texto))

temp_celcius = float(input('Digite a temperatura em celcius: '))
temp_fahrenheit = 32 + (temp_celcius * 9/5)
print(f'A temperatura {temp_celcius}° convertida para fahrenheit é: {temp_fahrenheit}°F')