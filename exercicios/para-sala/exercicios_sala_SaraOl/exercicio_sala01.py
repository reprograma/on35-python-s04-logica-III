# * Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido
# continue pedindo até que o usuário informe um valor válido.

nota = float(input('Insira uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    print('Valore inválido, tente novamente')
    nota = float(input('Insira uma nota de 0 a 10: '))
print('Eba, nota válida')
    
