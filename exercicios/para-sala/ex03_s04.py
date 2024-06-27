#Faça um programa que leia 5 números e informe o maior número.

#numeros = []  

#for info in range(5):
    #numero = int(input("Digite um número: "))   
    #numeros.append(numero)  
    #print (numeros)

#maior_numero=max(numeros)        

#print (f"O maior número é:{maior_numero}")      

# ou

maior_numero=0
for info in range (5):
    numero=float(input("Digite um número: "))
    if numero > maior_numero:
        maior_numero=numero

print (f"O maior número é:{maior_numero}")  