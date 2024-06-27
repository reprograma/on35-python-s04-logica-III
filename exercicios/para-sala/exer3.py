#Faça um programa que leia 5 números e informe o maior número.

numeros = []
for contador in range (5):
    numero = float(input(f"Insira o {contador + 1} número: "))
    numeros.append(numero)


maior_numero = max(numeros)
print(f'O maior númeuro entre os 5 é: {maior_numero}')