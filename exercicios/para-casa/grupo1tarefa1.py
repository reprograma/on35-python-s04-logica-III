# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input("Informe o número total de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for contador in range(1, total_eleitores + 1):
    voto = int(input(
        f"Eleitor {contador} - Digite o número do candidato em quem deseja votar: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Número inválido. Tente novamente")
        continue

print(f'\n Apuração dos votos:'
      f'\n Candidato 1 = {candidato1} votos'
      f'\n Candidato 2 = {candidato2} votos'
      f'\n Candidato 3 = {candidato3} votos')
