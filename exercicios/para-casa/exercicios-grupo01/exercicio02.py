# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
contador = 0

print("Numeros de 1 a 20 em lista: ")

while contador < 21:
    print(contador)
    contador += 1
else:
    print("Numeros de 1 a 20 em uma linha: ")
    for contador in range(1,21):
        print(contador, end= " ")