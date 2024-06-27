#* Desenvolva um gerador de tabuada:
# 1. capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# 2. O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:
#        Tabuada de 5:
#           5 X 1 = 5
#           5 X 2 = 10
#           ...
#           5 X 10 = 50


qual_tabuada = int(input('Qual a tabuada de 1 a 10 você gostaria de consulta?\nTabuada do: '))

for tabuando in range(1,11):
    resposta = qual_tabuada * tabuando
    print(f"{qual_tabuada:2} x {tabuando:2} = {resposta:3}")
