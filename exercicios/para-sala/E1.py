#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.


nota = int(input ("Por favor, insira uma nota de 0 a 10:  "))

while nota >10 or nota <0 :
    print("A nota inseriada foi inválida!")
    nota = int(input ("Por favor, insira uma nota de 0 a 10:  "))
else: 
    print("Obrigada por sua avaliação!")