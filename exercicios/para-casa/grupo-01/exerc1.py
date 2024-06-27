#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
numero_eleitores = int(input("Digite o número total de eleitores: "))
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for eleitor in range(numero_eleitores):
    print("Candidato 1\nCandidato 2\nCandidato 3")
    voto = int(input("Qual o candidato que voce vai votar: (insira o número: )"))
    if voto == 1:
        votos_candidato1 = votos_candidato1 + 1
    elif voto == 2:
        votos_candidato2 = votos_candidato2 + 1
    elif voto == 3:
        votos_candidato3 = votos_candidato3 + 1 
    else:  print("Candidato inválido") 
  
print("\nResultado:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")
