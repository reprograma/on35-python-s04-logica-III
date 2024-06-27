# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#  Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0

total_eleitores = int(input("Digite o número total de eleitores: "))

for i in range(total_eleitores):
    print("Vote no candidato (1, 2 ou 3):")
    voto = int(input(f"Eleitor {i+1}: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print(f"Resultado da eleição:")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")