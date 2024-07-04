#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Insira uma nota entre 0 e 10:' ' '))

while nota > 10:   
    nota = int(input(' Essa nota é Inválida \n Insira uma nota entre 0 e 10 novamente:' ' '))
else:
    print('Obrigada pela nota!')



    
    