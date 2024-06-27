# Exercício de Casa 🏠 

## Nome do Exercicio

## Grupo 1
#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

numero_de_cd=int(input("Digite a quantidade de CD: "))
valor_total=0

for colecionador in range(numero_de_cd):
    valor_cd = float(input(f"Digite o valor do CD {colecionador}: "))
    valor_total += valor_cd

    valor_medio = valor_total / numero_de_cd

print(f"O valor total investido na sua coleção de CDs é de R${valor_total:.2f}.")
print(f"Em média, você gastou R${valor_medio:.2f} por CD.")