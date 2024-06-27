#  Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
print ()
qtd_cds = int(input("Digite aqui a Quantidade de CDs da coleção \n"))
valor_investido = 0


for numero in range (qtd_cds):
    valor_cd = float(input(f"Digite o valor pago pelos cds {numero+1}\n"))
    valor_investido += valor_cd

if qtd_cds > 0:
    valor_medio = valor_investido/qtd_cds
else:
    valor_medio = 0

print(f"Valor total investido: R${valor_investido:.2f}\n")
print(f"Valor médio gasto por CD: R${valor_medio:.2f}\n")