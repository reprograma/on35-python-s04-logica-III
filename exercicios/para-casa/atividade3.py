numero_de_cd=int(input("Digite a quantidade de CD: "))
valor_total=0

for colecionador in range(numero_de_cd):
    valor_cd = float(input(f"Digite o valor do CD {colecionador}: "))
    valor_total += valor_cd

    valor_medio = valor_total / numero_de_cd

print(f"O valor total investido na sua coleção de CDs é de R${valor_total:.2f}.")
print(f"Em média, você gastou R${valor_medio:.2f} por CD.")