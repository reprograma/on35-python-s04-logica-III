# Exercício de Sala 🏫  
# 
# # Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.


def um_a_cinquenta():
  for num in range(1,51):
    if num % 2 != 0:
      print(num)


#-----------------------------------------


def um_cinquenta():    
  for num in range(1,51,2):
    print(num)

um_a_cinquenta()

um_cinquenta()