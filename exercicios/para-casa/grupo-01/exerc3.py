#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor pago em cada um.

quantidade=int(input("Quantos CD's voce tem?"))
total_investido=0

for cd in range(quantidade):
    preço=float(input(f"Quanto custou o CD {cd+1}?"))
    total_investido= total_investido+ preço

if quantidade>0:
    valor_medio = total_investido / quantidade
else: 
    valor_medio=0 
    
print(f"Voce investiu um total de R$ {total_investido:.2f} em CD's")
print(f"A média de investimentos foi de R$ {valor_medio:.2f}")
