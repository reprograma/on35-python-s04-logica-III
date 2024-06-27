# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f"O maior número digitado foi: {maior_numero}")