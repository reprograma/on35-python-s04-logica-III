# Exercício de Sala 🏫  Atividade 01
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.
notas = []
while True:
    nota = float(input("Digite uma nota entre 0 e 10 (ou digite -1 para parar): "))
    
    if nota == -1:
        break  
    
    if nota < 0 or nota > 10:
        print("Valor inválido. A nota deve estar entre 0 e 10.")
    else:
        notas.append(nota)  