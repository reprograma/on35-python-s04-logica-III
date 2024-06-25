# Faça um programa que leia 5 números e informe o maior número.

numeros_inseridos = []

for numeros in range(1,6):
    numeros_inseridos.append(int(input("Insira um número: ")))

print("O maior número inserido é:", max(numeros_inseridos))