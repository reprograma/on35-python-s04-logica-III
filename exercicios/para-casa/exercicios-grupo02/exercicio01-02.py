# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
tabuada = int(input("Insira a numero da tabuada a ser gerada: "))
for iterador in range(1,11):
    resultado = tabuada * iterador
    print(f"{tabuada} x {iterador} = {resultado}")
