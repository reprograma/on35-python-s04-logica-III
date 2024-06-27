# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


candidato_01 = 0
candidato_02 = 0
candidato_03 = 0

eleitores = int(input("Insira o número total de eleitores: "))

for iterador in range(eleitores):
    print('''
            VOTE NA SUA CANDIDATA:

            [1] - Ana
            [2] - Claudia
            [3] - Marta
  
        ''')

    voto = int(input('Escolha uma candidata: '))

    while voto not in [1, 2, 3]:
        voto = int(input("Candidato inválido, insira outro: "))

    if voto == 1:
        candidato_01 += 1
    elif voto == 2:
        candidato_02 += 1
    elif voto == 3:
        candidato_03 += 1

print("*** Total de votos ***")
print(f"Candidato 1: {candidato_01} votos")
print(f"Candidato 2: {candidato_02} votos")
print(f"Candidato 3: {candidato_03} votos")

if candidato_01 > candidato_02 and candidato_01 > candidato_03:
    print("Ana venceu a eleição")
elif candidato_02 > candidato_01 and candidato_02 > candidato_03:
    print("Claudia venceu a eleição")
elif candidato_03 > candidato_01 and candidato_03 > candidato_02:
    print("Marta venceu a eleição")
else:
    print("Houve um empate")
