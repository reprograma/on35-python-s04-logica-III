# Exercício de Casa 🏠 Grupo 1
## Atividade Eleitores e Candidatos

### Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao 
####final mostrar o número de votos de cada candidato.

numero_total_de_eleitores = int(input("digite o numero total de eleitores: "))

quantidade_votos_candidato1 = 0
quantidade_votos_candidato2 = 0
quantidade_votos_candidato3 = 0

for i in range (numero_total_de_eleitores): 
    print(f"eleitor {i + 1}")
    print("escolha o candidato 1, 2 ou 3")
    voto = int(input("candidato escolhido: "))

    if voto == 1:   
        quantidade_votos_candidato1 += 1
    elif voto == 2:
        quantidade_votos_candidato2 += 1
    elif voto == 3:
        quantidade_votos_candidato3 += 1
    else:
        print("voto inválido, vote novamente")
        i -= 1
    
print("\nresultados da eleicao:")
print(f"candidato 1: {quantidade_votos_candidato1} votos")
print(f"candidato 2: {quantidade_votos_candidato2} votos")
print(f"candidato 3: {quantidade_votos_candidato3} votos")



