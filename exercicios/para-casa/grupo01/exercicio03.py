# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um 
# deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds_total = int(input("Quantos CDs você possui no total: "))

lista_cds = []
valores_cd = []

for cds in range(cds_total):
    nome_cd = input(f"Nome do CD {cds+1}: ")
    valor_cd = float(input(f"Quanto custou este CD {cds+1}: "))


    lista_cds.append(nome_cd)   
    valores_cd.append(valor_cd)

dict_cds = {}

for nome, valor in zip(lista_cds, valores_cd):
    dict_cds[nome] = valor

valor_total = sum(valores_cd)
valor_medio = valor_total / cds_total


print("Dicionário de CDs e valores:")
print(dict_cds)

print(f"Valor total investido: R$ {valor_total:}")
print(f"Valor médio gasto por CD: R$ {valor_medio:}")




