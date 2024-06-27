
quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))

valor_total = 0

for i in range(1, quantidade_cds + 1):
    valor_cd = float(input(f"Digite o valor do CD {i}: "))
    valor_total += valor_cd

if quantidade_cds > 0:
    valor_medio = valor_total / quantidade_cds
else:
    valor_medio = 0

print(f"\nValor total investido: R$ {valor_total:.2f}")
print(f"Valor médio gasto por CD: R$ {valor_medio:.2f}")
