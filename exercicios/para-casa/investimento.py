# * Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.



valores_cd =[]

quantidade_cd = int(input("Coloque a quantidade de CDs: "))

for valor_cd in range (quantidade_cd):
    valor_cd = float(input("Digite o valor deste CDs: "))
    valores_cd.append (valor_cd)
    valor_investido = sum(valores_cd)
    valor_medio = valor_investido / quantidade_cd

print (f"Valores por cada CD: {valores_cd}")
print (f"Considerando a quantidade de CDs igual a {quantidade_cd} e o valor total investido de R$ {valor_investido}, \nvocê teve um valor médio de R$ {valor_medio} por CD.")