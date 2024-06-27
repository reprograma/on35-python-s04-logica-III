# Exercício de Casa 🏠 

## Nome do Exercicio

## Grupo 1
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidatos = ["Dilma", "Lula", "Haddad"]
votos = {
    "Dilma": 0,
    "Lula": 0,
    "Haddad": 0
}

numero_eleitores = int(input("Insira o número de eleitores: "))

for eleicao in range (numero_eleitores):
    while (voto := input("Insira o nome do seu candidato (Dilma, Lula, Haddad): ")) not in candidatos:
        print("Candidato inválido. Tente novamente.")
    votos[voto] += 1

print("\nResultado da votação:")
for candidato, numero_votos in votos.items():
    print(f"{candidato}: {numero_votos} votos")




        
