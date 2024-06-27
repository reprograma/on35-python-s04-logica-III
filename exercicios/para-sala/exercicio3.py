# Faça um programa que leia 5 números e informe o maior número.

lista= []
for numeros in range(1,6):
    lista.append(int(input('Digite numero: ')))
    
print('Maior número da lista: ', max(lista))




