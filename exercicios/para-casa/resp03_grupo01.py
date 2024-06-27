def calcular_investimento_cds():
    quantidade_cds = int(input("\nInforme a quantidade de CDs: "))
    total_investido = 0

    for i in range(1, quantidade_cds + 1):
        valor_unitario_cd = float(input(f"Informe o valor unitário do CD {i}: R$ "))
        total_investido += valor_unitario_cd
    
    media_investimento = total_investido / quantidade_cds

    print(f"\nTotal investido: R$ {total_investido:.2f}")
    print(f"Média do investimento: R$ {media_investimento:.2f}")

# Chamada da função para calcular investimento em CDs
calcular_investimento_cds()
