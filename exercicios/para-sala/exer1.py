#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Insira sua nota de zero a dez: "))

while nota > 10 or nota <0:
    print("Nota inválida. A nota deve estar entre 0 e 10.")

    nota = int(input("Insira sua nota de zero a dez: "))

print(f'{nota} é válida!')



