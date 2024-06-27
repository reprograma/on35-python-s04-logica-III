
# Faça um programa que leia 5 números e informe o maior número.
# num_lis = []

# for numero in range (0,5): 
#     numeros = int(input("digite um numero:"))
#     num_lis.append(numeros)
#     print(num_lis)

# maior_numero = max(num_lis)
# print(maior_numero)


maior_numero = 0

for contador in range (5):
    numero = int(input("digite um numero:"))
    if numero > maior_numero:
        maior_numero = numero

print(maior_numero)

