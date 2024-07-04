#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def main():
    num_eleitores = int(input("Digite o número total de eleitores: "))
    
    votos_candidato1 = 0
    votos_candidato2 = 0
    votos_candidato3 = 0
    
    for eleitor in range(1, num_eleitores + 1):
        print(f"Eleitor {eleitor}:")
        print("Digite o número correspondente ao candidato que deseja votar:")
        print("1 - Candidato 1")
        print("2 - Candidato 2")
        print("3 - Candidato 3")
        
        voto = int(input("Digite sua escolha (1, 2 ou 3): "))
        
        if voto == 1:
            votos_candidato1 += 1
        elif voto == 2:
            votos_candidato2 += 1
        elif voto == 3:
            votos_candidato3 += 1
        else:
            print("Voto inválido. Eleitor não votou em nenhum candidato.")
    
    print("\nResultado da votação:")
    print(f"Votos do Candidato 1: {votos_candidato1}")
    print(f"Votos do Candidato 2: {votos_candidato2}")
    print(f"Votos do Candidato 3: {votos_candidato3}")

if __name__ == "__main__":
    main()