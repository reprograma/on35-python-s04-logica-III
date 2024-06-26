# Faça um programa que leia 5 números e informe o maior número.

lista_numeros = []

for contador in range(1, 6):
    lista_numeros.append(int(input("Digite um número: ")))

print(f'O maior número da lista é {max(lista_numeros)}')
