# Exercício de Casa - Grupo 1🏠 

# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtd_cds = int(input('qts CDs você comprou? '))

preco_total = 0

for i in range(0,qtd_cds):
    preco_cds = float(input(f'Qual o preço do {i+1}º CD? R$ '))
    preco_total = preco_total + preco_cds
    i = i + 1

preco_medio = preco_total/qtd_cds

print(f'O preço médio dos CDs foi R$ {preco_medio}')