#  Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.


quantidade_cds = int(input("Diga a quantidade de CDs na coleção: "))

valor_total = 0

for i in range(quantidade_cds):
    valor_cd = float(input(f"Informe o valor do CD {i+1}: "))
    valor_total += valor_cd

if quantidade_cds > 0:
    valor_medio = valor_total / quantidade_cds
else:
    valor_medio = 0

print(f"\nValor total investido: R$ {valor_total:.2f}")
print(f"Valor médio gasto por CD: R$ {valor_medio:.2f}")