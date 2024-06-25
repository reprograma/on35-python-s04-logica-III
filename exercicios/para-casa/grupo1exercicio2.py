# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

# Um abaixo do outro
interador = 0

for interador in range(1,21):
    print(interador)

# Um do lado do outro
interador = 1

for interador in range(1,21):
    print(interador, end=' ')