import math

# Tamanho da área a ser pintada em metros quadrados
area_a_pintar = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade de litros de tinta necessários
litros_tinta = area_a_pintar / 3

# Calcula a quantidade de latas de tinta necessárias
quantidade_latas = math.ceil(litros_tinta / 18)

# Calcula o preço total das latas de tinta
preco_total = quantidade_latas * 80

# Exibe a quantidade de latas de tinta e o preço total
print(f"Você precisará comprar {quantidade_latas} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")
