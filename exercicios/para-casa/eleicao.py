# * Numa eleição existem três candidatos. 
# Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votos_canditados1 = 0
votos_canditados2 = 0
votos_canditados3 = 0

numero_eleitores= int(input("Quantos eleitores tem essa eleição?:  "))

for eleicao in range(0,numero_eleitores):
    voto = int(input("Escolha um dos candidatos abaixo: \n"
                   "Joao vote 1 \n"
                   "Maria vote 2 \n"
                   "Pedro vote 3: \n"))

    if voto ==1:
        votos_canditados1 += 1
    elif voto ==2:
        votos_canditados2 += 1
    elif voto ==3:
        votos_canditados3 += 1
    else:
        print("Seu voto é invalido")
        voto = int(input("Escolha um dos candidatos abaixo: n/"
                   "Joao vote 1 \n"
                   "Maria vote 2 \n"
                   "Pedro vote 3: \n"))

print(f"O candidato 1 teve {votos_canditados1}votos,O candidato 2 teve {votos_canditados2}votos, o candidato 3 teve {votos_canditados3}votos")
    