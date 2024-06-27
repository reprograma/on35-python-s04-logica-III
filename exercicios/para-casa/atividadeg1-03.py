# Exercício de Casa 🏠 Grupo 1 - Atividade Calculadora de Investimentos - Coleção de CDs.

##Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
### o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtd_cds = int(input("digite a qtd de cds: "))
print("")

valor_total = 0

for i in range(qtd_cds):
    valor_cd = float(input("digite o valor de cada cd {}: " .format(i + 1)))
    valor_total += valor_cd

valor_medio = valor_total / qtd_cds

print("")
print("valor total gasto: R$", valor_total)
print("valor medio gasto por cada cd: R$", valor_medio)

