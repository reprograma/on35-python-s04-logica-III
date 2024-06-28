#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cd = int(input('Digite o número de CD: '))
valor_total = 0
valor_medio = 0

for i in range (quantidade_cd):
    valor_cd = float(input(f'Digite o valor do CD {i+1}: ')) 
    valor_total += valor_cd

print(f'Valor total é: {valor_total}')
print(f'Valor médio é: {valor_total/quantidade_cd}')