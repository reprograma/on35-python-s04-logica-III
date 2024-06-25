# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada.

numero = int(input("Digite um número: "))
multiplicar = 1

print(f"A tabuada de {numero} é: ")

for operacao in range(10):
    tabuada = numero * multiplicar
    print(f'{numero} X {multiplicar} = {tabuada}')
    multiplicar = multiplicar + 1