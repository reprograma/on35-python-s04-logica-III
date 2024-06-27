quantidade_eleitores = int(input("\nDigite o número de eleitores: "))

def realizar_eleicao():
    dandara_palmares = 0
    makota_valdina = 0
    carolina_maria = 0

    for i in range(quantidade_eleitores):
        print("-" * 30)
        print("        VOTAÇÃO    ")
        print("-" * 30)
        print("[1] - Dandara dos Palmares")
        print("[2] - Makota Valdina")
        print("[3] - Carolina Maria de Jesus")

        voto = input(f"\nEleitor {i+1} informe seu voto: ")
                   
        if voto == "1":
            dandara_palmares += 1
        elif voto == "2":
            makota_valdina += 1
        elif voto == "3":
            carolina_maria += 1
        else:
            print("Opção inválida. Voto não computado.")

    print(
        "Votação encerrada!\n"
        "\n *** RESULTADO DA ELEIÇÃO ***\n    "
        f"\nDandara dos Palmares: {dandara_palmares} voto(s)"
        f"\nMakota Valdina: {makota_valdina} voto(s)"
        f"\nCarolina Maria de Jesus: {carolina_maria} voto(s)\n")


realizar_eleicao()

