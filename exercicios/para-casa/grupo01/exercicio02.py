# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.


contador = 1
while (contador < 21):
      print(contador)
      contador = contador + 1
else:
    for num in range(1, 21):
         print(num, end=" ")