## Grupo 1


def main():
    total_eleitores = int(input("Digite o número total de eleitores: "))
    
    zezo_do_mercadinho = 0
    irmao_da_harpa = 0
    pastora_josilene = 0
    
    for eleitor in range(1, total_eleitores + 1):
        print(f"Eleitor {eleitor}, por favor vote:")
        print("1 - Zezo do Mercadinho")
        print("2 - Irmão da Harpa")
        print("3 - Pastora Josilene")
        
        voto = int(input("Digite o número do candidato em que deseja votar: "))
        
        if voto == 1:
            zezo_do_mercadinho += 1
        elif voto == 2:
            irmao_da_harpa += 1
        elif voto == 3:
            pastora_josilene += 1
        else:
            print("Opção inválida. Voto não contado.")
    
    print("\nResultado da eleição:")
    print(f"Zezo do Mercadinho: {zezo_do_mercadinho} votos")
    print(f"Irmão da Harpa: {irmao_da_harpa} votos")
    print(f"Pastora Josilene: {pastora_josilene} votos")

# Chamada direta da função main()
main()



# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

print("De 1 a 20, um abaixo do outro:")
for iterador in range(1, 21):
    print(iterador)

print("De 1 a 20, mas um ao lado do outro:")
for iterador in range(1, 21):
    print(iterador, end=" ")


#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

    quant_cds = int(input("Digite a quantidade de CDs que você possui: "))
    valor_total_investido = 0

    for cd in range(1, quant_cds + 1):
        valor_cd = float(input(f"Digite o valor do CD {cd}: "))
        valor_total_investido += valor_cd
    
    if quant_cds > 0:
        valor_medio = valor_total_investido / quant_cds
    else:
        valor_medio = 0.0  
    
    print(f"O valor total investido em {quant_cds} CDs é: R$ {valor_total_investido:.2f}")
    print(f"O valor médio gasto por CD é: R$ {valor_medio:.2f}")
    break

