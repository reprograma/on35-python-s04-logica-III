lista = [1,2,6,8,9,7,5,8,10]

print(lista[-1])
print(lista[-2])
print(lista[-5])

lista1 = ['um',2,3.14,[10,20,30]]
print(lista1[0])
print(lista1[3][0]) #O terceiro elemento é uma lista. O comando é: "imprima o elemento 0 do elemento 3 que é uma lista"

lista2 = ['um','dois',3,6,5,[30,20,10]]
print(lista2[0:3]) #Imprima do 0 até o 2 (nao inclui o quarto elemento (que no caso é o 3º))

print(lista2[:]) #Imprime todos
print(lista2[2:]) #Imprime desde o segundo elemento (3) até o final da lista
print(lista2[:3]) #Imprime desde o inicio até o elemento 2 (3)