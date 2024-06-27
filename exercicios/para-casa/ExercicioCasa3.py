quantidadeCD = int(input("Informe a quantidade de CD: "))
valorTotal = 0

for i in range(1, quantidadeCD + 1):
    valorCD = float(input(f"Informe o valor do CD {i}: "))
    valorTotal += valorCD

valorMedio = valorTotal / quantidadeCD

print(f"Valor total: R$ {valorTotal:.2f}")
print(f"Valor médio por CD: R$ {valorMedio:.2f}")
