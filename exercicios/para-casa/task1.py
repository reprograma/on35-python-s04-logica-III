# * Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votes_lula = 0
votes_jose = 0
votes_maria = 0

voters = int(input("Digite o número de eleitores: "))

for election in range(0, voters):
    vote = int(input("Escolha um candidato: \n-Lula, \n-José ou \n-Maria \n-Responda com o número 1, 2 ou 3: "))
    if vote == 1:
        votes_lula += 1
    elif vote == 2:
        votes_jose += 1
    elif vote == 3:
        votes_maria += 1    
    else:
        print("Voto inválido. Por favor, vote 1, 2 ou 3.")
    
# show results
print("\nResultado da votação:")
print(f"Lula: {votes_lula} voto(s)")
print(f"José: {votes_jose} voto(s)")
print(f"Maria: {votes_maria} voto(s)")