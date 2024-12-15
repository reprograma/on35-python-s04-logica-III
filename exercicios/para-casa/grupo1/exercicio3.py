# Exercício de Casa 🏠 

## Nome do Exercicio

## Grupo 1
#* Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("informe a quantidade de cds da sua coleção: "))

valores_cds=[]

for coleção in range(cds):
    valor_por_cd = float(input("informe o valor de cada cd: "))
    valores_cds.append(valor_por_cd)

valor_total_investido = sum(valores_cds)
quantidade_cds = cds

valor_medio = valor_total_investido / quantidade_cds
print(f"O valor médio de cada cd é R${valor_medio:.2f}")
