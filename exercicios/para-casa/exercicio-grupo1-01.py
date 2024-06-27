
def eleicao():
    print("Benvindo, faça uma boa escolha!")
    
    candidatos = ["Dilmãe", "Lula lindo", "Boulos"]
    
    votos = {candidato: 0 for candidato in candidatos}
    
    total_eleitores = int(input("Digite o número total de eleitores: "))
    
    for i in range(total_eleitores):
        print("\nEleitor", i + 1)
        print("Escolha um candidato:")
        for j in range(len(candidatos)):
            print(f"{j + 1}. {candidatos[j]}")
        
        voto = int(input("Digite o número do candidato escolhido: "))
        
        if 1 <= voto <= len(candidatos):
            candidato_escolhido = candidatos[voto - 1]
            votos[candidato_escolhido] += 1
        else:
            print("Voto inválido! Tente novamente.")
            i -= 1  
    
    print("\nResultados da eleição:")
    for candidato in candidatos:
        print(f"{candidato}: {votos[candidato]} voto(s)")

eleicao()

