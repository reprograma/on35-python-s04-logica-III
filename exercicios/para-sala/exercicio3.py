#Faça um programa que leia 5 números e informe o maior número.

numeros = []
for contador in range(5):
    numero = int(input('Digite o número:'))
    numeros.append(numero)

maior_numero = max(numeros)
print (f'O número maior é: {maior_numero}')  

 



