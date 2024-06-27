#Faça um programa que leia 5 números e informe o maior número.
# usar loop, list, apende e if.
# imput dentro de um loop e a partir desse loop fazer isso 5 vezes

lista = []
for numeros in range (1,6):
    lista.append(int(input("Insira um novo numero para analise: ")))
print ("Maior numero da lista: ", max(lista))