#Faça um programa que leia 5 números e informe o maior número.
numeros = [5, 10, 15, 20, 25]

maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número é o: {maior_numero}")