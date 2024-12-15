# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 
#Quanto a pessoa já gastou no total
# valor médio gasto
# a pessoa vai inserir o valor de cada cd
# quantidade total gasta
# média do valor gasto

valores_cd = []
quantidade_cds = int(input ("Informe quantos cds você possui: "))

for valor_cd in range (quantidade_cds):
    valor_cd = float(input("Digite o valor de cada CD, um por vez: "))
    valores_cd.append (valor_cd)
    valor_total_investido = sum(valores_cd)
    valor_medio = valor_total_investido / quantidade_cds

    print (f"Valores por cada CD: {valores_cd}")
    print (f"O valor total gasto é de {valor_total_investido} e o valor médio de cada CD é de {valor_medio}")





