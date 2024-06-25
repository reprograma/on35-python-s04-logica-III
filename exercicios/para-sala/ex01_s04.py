# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Coloque uma nota entre 0 e 10: "))
while not nota in range(11):     # while nota>10 or nota<0:
    print("Nota inválida") 
    nota = int(input("Coloque uma nota entre 0 e 10: "))

print (f"Sua nota é {nota}")  
