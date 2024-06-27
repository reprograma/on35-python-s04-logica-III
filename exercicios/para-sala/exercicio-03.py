# Faça um programa que leia 5 números e informe o maior número.

maior_numero = 0
for contador in range (5):
       numero = float(input( f"Insira o número: "))
       if numero > maior_numero:
              maior_numero = numero
              
             
       

print(f"O maior número entre os 5 é: {maior_numero}")