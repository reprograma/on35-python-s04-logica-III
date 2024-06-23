# * Faça um programa que leia 5 números e informe o maior número.

armazena_num = []

for contagem in range(5):
    lendo_numeros = float(input(f'Insira um número {contagem+1}: '))
    armazena_num.append(lendo_numeros)

maior_numero = max(armazena_num)
print(f"O maior número é: {maior_numero}")

