# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cd = int(input("Informe a quantidade de CDs: "))

valores_cd = 0

for contador in range(1, quantidade_cd+1):
    valores_cd += float(input(f'Digite o valor do {contador}º CD: '))

valor_medio = valores_cd / quantidade_cd

print(f'\n O valor médido gasto em cada CD é R${valor_medio:.2f}. \n')
