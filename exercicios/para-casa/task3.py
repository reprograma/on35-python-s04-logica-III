# * Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cd_values = []

quant_cds = int(input("Informe a quantidade total de CDs: "))
total_value = 0.0

for cd_value in range (quant_cds):
    cd_value = float(input("Informe o valor deste CD: "))
    cd_values.append (cd_value)
    total_value = sum(cd_values)
    average_value = total_value / quant_cds

print (f"Valores investidos em cada CD: {cd_values}")
print (f"Valor médio por CD considerando a quantitade de {quant_cds} CDs e o valor total de R$ {total_value}: R$ {average_value}")