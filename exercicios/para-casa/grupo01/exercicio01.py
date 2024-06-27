# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input("Insira o total de eleitores dessa zona eleitoral: "))

votos = []

print("\n Candidatos a Eleição: \n 1 - Rony Weasley \n 2 - Draco Malfoy \n 3 - Cho Chang")

for eleitor in range(eleitores):
    voto_eleitor = int(input(f"Eleitor {eleitor+1} insira o número do seu candidato: "))

    if voto_eleitor in [1 , 2, 3]:
        votos.append(voto_eleitor)
    else: 
        print("Opção inválida. Voto Anulado")

votos_candidato1 = votos.count(1)
votos_candidato2 = votos.count(2)
votos_candidato3 = votos.count(3)

print("\nResultado da eleição:")
print(f"Rony Weasley: {votos_candidato1} votos")
print(f"Draco Malfoy: {votos_candidato2} votos")
print(f"Cho Chang: {votos_candidato3} votos")


