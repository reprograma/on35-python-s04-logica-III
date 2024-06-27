# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def eleicao():

    eleitores = int(input("Quantos eleitores vão votar: "))

    for i in range(eleitores):
        print(f"Eleitor {i + 1}")
        voto = int(input("Quem você quer para presidenta do Brasil: \n Vote 1: Ludmilla \n Vote 2: Pabllo Vittar \n Vote 3: Gloria Groove \n Seu Voto: "))

        if voto == 1:
            ludmila += 1
        elif voto == 2:
            pabllo_vittar += 1
        elif voto == 3:
            gloria_groove += 1
        else:
            print("Voto inválido. Tente novamente.")
            i -= 1

    print("\nResultado da eleição para presidenta do Brasil:")
    print(f"Ludmila: {ludmila} votos")
    print(f"Pabllo Vittar: {pabllo_vittar} votos")
    print(f"Gloria Groove: {gloria_groove} votos")

eleicao()