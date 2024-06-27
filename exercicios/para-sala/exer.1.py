# * Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
# o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def pedir_nota():
    while True:
        try:
            nota = float(input("Informe uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                print(f"Nota válida: {nota}")
                break
            else:
                print("Valor inválido. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

pedir_nota()

# Outra forma de responder:

nota = float(input("Informe uma nota entre 0 e 10: "))

while nota > 10 or nota < 0:
    print("Nota inválida, favor, informar novamente")
    nota = float(input("Informe uma nota entre 0 e 10: "))

else:
    print(f"A {nota} é inválida")

        


