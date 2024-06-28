# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio 
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

valores_cd_armazenado = []
qtd_cd = int(input("Informe a quantidade de CD's da sua coleção: "))

for valor_cd_informado in range(qtd_cd):
    valor_cd_informado = float(input(f"Qual o valor em reais do CD {valor_cd_informado + 1}: "))
    valores_cd_armazenado.append(valor_cd_informado)
    qtd_total_valores = sum(valores_cd_armazenado)
    valor_medio = qtd_total_valores/qtd_cd

print("\nResultados da Coleção:")    
print(f"Valor total da coleção R$ {qtd_total_valores:.2f}")
print(f"Valor médio por CD da coleção R$ {valor_medio:.2f}")


