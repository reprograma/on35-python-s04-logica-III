eleitores = int(input("Digite o número de eleitores: "))
votos = []

for eleitor in range(eleitores):
    voto = int(input(f"Eleitor {eleitor+1} Digite o número do candidato (1 em diante): "))
    if voto > len(votos):
        votos += [0] * (voto - len(votos))
    votos[voto - 1] += 1

for candidata, votos_candidata in enumerate(votos):
    print(f"Candidata {candidata + 1}: {votos_candidata} voto(s)")