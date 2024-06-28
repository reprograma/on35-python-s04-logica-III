#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
total_de_eleitores = int(input('Digite o numero de eleitores: '))

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

for eleitor in range(total_de_eleitores):
    print(f'Eleitor número {eleitor+1}')

    print('Digite 1 para votar Candidato 1 \nDigite 2 para votar Candidato 2 \nDigite 3 para votar Candidato 3')

    vote = int(input('Digite seu voto: '))

    if vote == 1:
        votos_candidato_1 += 1
    elif vote == 2:
        votos_candidato_2 += 1
    elif vote == 3:
        votos_candidato_3 += 1
    else:
        print('Voto inválido.')

print(f'Resultado da eleição: \nCandidato 1: {votos_candidato_1} \nCandidato 2: {votos_candidato_2} \nCandidato 3: {votos_candidato_3}')