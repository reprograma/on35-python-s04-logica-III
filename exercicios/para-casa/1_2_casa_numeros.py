# Exercício de Casa - Grupo 1 🏠 

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

lista = []

for i in range(1,21):
    print(i)
    lista.append(i)
    i = i + 1
print(lista)