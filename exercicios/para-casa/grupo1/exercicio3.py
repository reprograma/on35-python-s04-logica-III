# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o 
# valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_CD = int(input("Insira a quantidade de CDs da coleção: "))
valores_CD = []

for calculo in range (quantidade_CD):
    valor_CD = float(input(f"Insira o valor de cada CD: "))
    valores_CD.append(valor_CD)

total_colecao = sum(valores_CD)
print(f"O valor total gasto na coleção foi de R$ {total_colecao}")

media_colecao = total_colecao/quantidade_CD
print(f"A média de valor da coleção é de R$ {media_colecao} por CD")


    