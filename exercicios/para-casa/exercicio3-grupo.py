quantidade_cds = int(input("Informe a quantidade de CDs comprados: "))
valor_cd = float(input("Informe o valor pago por cada CD: "))

valor_total = quantidade_cds * valor_cd

valor_medio = valor_total / quantidade_cds if quantidade_cds else 0

print(f"\nValor total gasto: R$ {valor_total:.2f}")
print(f"Valor médio gasto por CD: R$ {valor_medio:.2f}")