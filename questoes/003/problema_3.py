fahrenheit = float(input('Informe a temperatura em F°: '))

trans_cels = round(5 * ((fahrenheit - 32) / 9), 2)

print(f'{fahrenheit} F° transformado em Celsius é: {trans_cels}°')