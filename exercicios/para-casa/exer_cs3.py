# * Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
# e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs 
# e o valor para em cada um.

def cds_quantidade():

    cds_quantidade = int(input("Quantos CDs o colecionar têm: "))

    valor_cd_total = 0

    for i in range(cds_quantidade):
        print(f"CD {i+1}")
        valor_cd = float(input(f"Qual o valor do CD {i+1}: "))
        valor_cd_total += valor_cd

    if cds_quantidade > 0:
        valor_cd_media = valor_cd_total / cds_quantidade
    
    else:
        valor_cd_media = 0

    print(f"O valor total pago nos CDs da coleção foi de R$ {valor_cd_total}")
    print(f"O valor médio pago nos CDs é de {valor_cd_media}")

cds_quantidade()
