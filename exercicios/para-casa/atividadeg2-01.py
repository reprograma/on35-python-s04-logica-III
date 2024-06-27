#Exercício de Casa 🏠 Grupo 2 - Atividade Tabuada do 1 ao 10 
##Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
### numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: Tabuada de 5: 5 X 1 = 5, 5 X 2 = 10...5 X 10 = 50.

while True:
    try:
        
        gerador_de_resultados_tabuada = int(input("Escolha a tabuada do 1 ao 10 para obter os resultados: "))
        if 1 <= gerador_de_resultados_tabuada <= 10:
            break
        else:
            print("Por favor, informe um número entre 1 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, informe um número inteiro.")

print(f"\nTabuada de {gerador_de_resultados_tabuada}:")

for i in range(1, 11):
    resultado = gerador_de_resultados_tabuada * i
    print(f'gerador_de_resultados_tabuada * {i} = {resultado}')