def main():
    totalEleitores = int(input("Digite o número total de eleitores: "))
    
    votosCandidato1 = 0
    votosCandidato2 = 0
    votosCandidato3 = 0
    
    for eleitor in range(1, totalEleitores + 1):
        print(f"Eleitor {eleitor}:")
        print("Digite 1 para votar no Candidato 1")
        print("Digite 2 para votar no Candidato 2")
        print("Digite 3 para votar no Candidato 3")
        voto = int(input("Digite o número do candidato em quem você deseja votar: "))
        
        if voto == 1:
            votosCandidato1 += 1
        elif voto == 2:
            votosCandidato2 += 1
        elif voto == 3:
            votosCandidato3 += 1
        else:
            print("Voto inválido. Eleitor não votou em nenhum candidato.")
    
    print("\nResultado da eleição:")
    print(f"Total de votos do Candidato 1: {votosCandidato1}")
    print(f"Total de votos do Candidato 2: {votosCandidato2}")
    print(f"Total de votos do Candidato 3: {votosCandidato3}")

main()