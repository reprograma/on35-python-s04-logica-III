# Faça um programa que leia 5 números e informe o maior número.

numero_armazenado = [1]

for contator in range (5):
    numero_informado = float(input("Por gentileza,digite um número: "))
    numero_armazenado.append(numero_informado)

numero_maior = max(numero_armazenado)
print(f"O maior numero é: {numero_maior}")

print(numero_armazenado)