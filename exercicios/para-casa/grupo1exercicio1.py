# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input("Insira o total de eleitores: "))

cand1 = 0
cand2 = 0
cand3 = 0

for votos in range(total_eleitores):
    escolha = input("Vote em A, B ou C: ").lower()

    if escolha == "a":
        cand1 = cand1 + 1
    elif escolha == "b":
        cand2 = cand2 + 1
    elif escolha == "c":
        cand3 = cand3 + 1
    else:
        print("Escolha inválida. Voto não contabilizado.")

print(f"O candidato A ficou com {cand1} votos.")
print(f"O candidato B ficou com {cand2} votos.")
print(f"O candidato C ficou com {cand3} votos.")