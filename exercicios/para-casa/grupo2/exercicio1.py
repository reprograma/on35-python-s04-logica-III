## Grupo 2
#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:



numero = int(input("insira o número da tabua: "))

tabuada=[]
for sequencia in range(1,11):
       resulatado = numero * sequencia
       expressao = f"{numero} x {sequencia} = {resulatado}"
       tabuada.append(expressao)

print(f"A tabuada do {numero}:")

for item in tabuada:
    print(item)