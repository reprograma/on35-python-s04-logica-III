candidatos = ["Dilma", "Lula", "Haddad"]
votos = {
    "Dilma": 0,
    "Lula": 0,
    "Haddad": 0
}

num_eleitores = int(input("Insira o número de eleitores: "))

for eleicao in range (num_eleitores):
    while (voto := input("Insira o nome do seu candidato (Dilma, Lula, Haddad): ")) not in candidatos:
        print("Candidato inválido. Tente novamente.")
    votos[voto] += 1

print("\nResultado da votação:")
for candidato, num_votos in votos.items():
    print(f"{candidato}: {num_votos} votos")