# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
numero_de_cds = int(input("Insira o numero total de cds da sua colecao: "))
valor_total = 0
for iterador in range(numero_de_cds):
    preco_cd = float(input("Insira o preço pago no CD: "))
    valor_total = valor_total + preco_cd

preco_medio = valor_total/numero_de_cds

print(f"Preço médio pago por CD: R$ {preco_medio:.2f}")

