#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Insira uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print (f"Nota {nota} inválida, digite novamente")
    nota = int(input("Insira uma nota entre 0 e 10: "))

print(f"Nota {nota} aceita!")
    
    
# uso do else não é recomendado com o while nesse contexto.