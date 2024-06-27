# * Faça um programa que leia 5 números e informe o maior número.

numeros = []

for contador in range(5):
    numero = float(input(f"Infome o número {contador + 1}º numero: "))
    numeros.append(numero)
    print(numeros)

maior_numero = max(numeros)
print(f"O maior número entre os 5 é : {maior_numero}")
