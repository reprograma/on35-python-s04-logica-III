# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade_cds =int(input("Informe a quantidade de CDs "))
valor_total_investido = 0.0

for cd in range(quantidade_cds):
    valor_cd = float(input(f"Informe o valor gasto no CD {cd}: R$ "))
    valor_total_investido += valor_cd 

if quantidade_cds > 0:
    valor_por_cd = valor_total_investido / quantidade_cds
else:
        valor_por_cd = 0.0 

print("Resumo da coleção de CDs:")
print(f"Valor total investido: R$ {valor_total_investido}")
print(f"Valor médio gasto por CD: R$ {valor_por_cd}")