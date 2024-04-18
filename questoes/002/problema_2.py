# Solicita as notas bimestrais do usuário
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Calcula a média aritmética e arredonda para uma casa decimal
media = round((nota1 + nota2 + nota3 + nota4) / 4, 1)

# Exibe a média
print("A média aritmética do ano é: ", media)
