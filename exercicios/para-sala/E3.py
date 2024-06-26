# Faça um programa que leia 5 números e informe o maior número.

lista = []

for numero in range(1,6):
    lista.append(int(input('Por favor, digite um número: ')))

maior = max(lista)
print (f"O maior número é: {maior}")


