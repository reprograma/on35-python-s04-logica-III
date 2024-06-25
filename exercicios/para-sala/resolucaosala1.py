# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota:
    if nota >= 0 and nota <= 10:
        print(f"Você digitou a nota {nota}.")
        break
    else:
        print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")

