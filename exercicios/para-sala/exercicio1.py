# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:

    nota = float(input("Informe a nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida")
    else:
        print(f"A nota informada é {nota}")
        break
