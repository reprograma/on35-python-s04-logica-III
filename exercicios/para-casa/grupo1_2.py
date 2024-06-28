# Solicita o número total de eleitores
num_eleitores = int(input("Digite o número total de eleitores: "))

# Inicializa os contadores de votos para os três candidatos
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

# Loop para pedir o voto de cada eleitor
for i in range(num_eleitores):
    print(f"Eleitor {i + 1}, vote em um dos candidatos:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    
    voto = int(input("Digite o número do candidato escolhido: "))
    
    # Conta o voto para o candidato correspondente
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido! Tente novamente.")

# Exibe o número de votos de cada candidato
print("\nResultados da eleição:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")
