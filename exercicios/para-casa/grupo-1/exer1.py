# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def votacao():
    num_eleitores = int(input("Digite o número total de eleitores: "))
    
    votos = [0, 0, 0]
    
    for eleitor in range(num_eleitores + 1):
        print(f"Eleitor {eleitor}, vote:")
        print(" 1- Candidato 1")
        print(" 2- Candidato 2")
        print(" 3- Candidato 3")
        voto = int(input("Digite o número do seu candidato: "))
        
        
        if 1 <= voto <= 3:
            votos[voto - 1] += 1  
        else:
            print("Voto inválido! Eleitor não votou.")
    
    
    print("Resultado da eleição:")
    for candidato in range(3):
        print(f"Candidato {candidato + 1}: {votos[candidato]} votos")

if __name__ == "__main__":
    votacao()
