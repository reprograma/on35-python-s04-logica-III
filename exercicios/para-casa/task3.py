# * Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quant_cds = int(input("Informe a quantidade de CDs na coleção: "))
valor_total_investido = 0.0

for i in range(quant_cds):
        valor_cd = float(input(f"Informe o valor pago pelo CD {i+1}: "))
        valor_total_investido += valor_cdif quant_cds > 0:
    valor_medio = valor_total_investido / quantidade_cds
else:
valor_medio = 0.0
    
print(f"\nValor total investido: R$ {valor_total_investido:.2f}")
print(f"Valor médio gasto por CD: R$ {valor_medio:.2f}")

if __name__ == "__main__":
    main()