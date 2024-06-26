
quantidade_eleitores = int(input("\nDigite o número de eleitores: "))

def realizar_eleicao():
    votos_candidato_1 = 0
    votos_candidato_2 = 0
    votos_candidato_3 = 0

    for i in range(quantidade_eleitores):
        print("-" * 30)
        print("        VOTAÇÃO    ")
        print("-" * 30)
        print("[1] - Dandara dos Palmares")
        print("[2] - Makota Valdina")
        print("[3] - Carolina Maria de Jesus")

        voto = input(f"\nEleitor {i+1} informe seu voto: ")
                   
        if voto == "1":
            votos_candidato_1 += 1
        elif voto == "2":
            votos_candidato_2 += 1
        elif voto == "3":
            votos_candidato_3 += 1
        else:
            print("Opção inválida. Voto não computado.")

    print(
        "Votação encerrada!\n"
        "\n *** RESULTADO DA ELEIÇÃO ***\n    "
        f"\nDandara dos Palmares: {votos_candidato_1} voto(s)"
        f"\nMakota Valdina: {votos_candidato_2} voto(s)"
        f"\nCarolina Maria de Jesus: {votos_candidato_3} voto(s)\n")


realizar_eleicao()

