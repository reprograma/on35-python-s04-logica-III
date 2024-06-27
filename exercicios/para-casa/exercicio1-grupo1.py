eleitores = int(input("Digite o número de eleitores: "))
votos = []

for eleitor in range(eleitores):
    voto = int(input(f"Eleitor {eleitor+1} Digite o número do candidato: "))
    if voto > len(votos):
        votos += [0] * (voto - len(votos))
    votos[voto - 1] += 1

candidata = 1
for votos_candidata in votos:
    print(f"Candidata {candidata}: {votos_candidata} voto(s)")
    candidata += 1