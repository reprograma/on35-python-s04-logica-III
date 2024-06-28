# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

numero = int(input("Por gentileza, insira um número de 0 a 10: \n"))

while numero < 0 or numero > 10 :
    print(f"O número {numero} esta fora do intervalo solicitado.")
    numero = int(input("Por gentileza, insira um número de 0 a 10: \n"))

print(f"O número {numero} esta dentro do intervalo solicitado.")  