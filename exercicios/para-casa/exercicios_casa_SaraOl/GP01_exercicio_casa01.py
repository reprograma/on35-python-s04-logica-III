# * Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar
# Ao final mostrar o número de votos de cada candidato.

# Variável que irá armazenar os votos
candidato01 = 0
candidato02 = 0
candidato03 = 0
    
total_eleitores = int(input('Insira a quantidade total de eleitores: '))

# O range utilza a variável total_eleitores como componente para retornar a quantidade de eleitores disponíveis.
# O laço For intera o código mostrando os candidatos e armazenando cada respectivo voto em sua variável.
for num_eleitores in range(total_eleitores):
    hora_de_votar = int(input(f"Digite 10 para votar no Canditato 1\nDigite 20 para votar no Canditato 2 e\nDigite 30 para votar no Canditato 3\nInsira sua resposta eleitore {num_eleitores+1}: "))
    if hora_de_votar == 10:
        candidato01 += 1
    elif hora_de_votar == 20:
        candidato02 += 1
    elif hora_de_votar == 30:
        candidato03 += 1
    else:
        print('Código inválido, tente novamente!')

print(f"O total de votos do Candidato 1 foi de: {candidato01}")
print(f"O total de votos do Candidato 2 foi de: {candidato02}")
print(f"O total de votos do Candidato 3 foi de: {candidato03}")
