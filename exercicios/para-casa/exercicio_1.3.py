# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 
#Quanto a pessoa já gastou no total
# valor médio gasto
# a pessoa vai inserir o valor de cada cd
# quantidade total gasta
# média do valor gasto

quantidade_cds = int(input ("Informe quantos cds você possui: "))
colecao_cds = {}

for cd in range (quantidade_cds):
    valor = float(input(f"Informe o valor do CD {cd + 1}: "))
    colecao_cds[F"CD {cd + 1}"] = {"Valor": valor}

print("Coleção de CDs: ")
for cd, info in colecao_cds.items():
    print(f"{cd}: R${info["Valor"]:.2f}")





