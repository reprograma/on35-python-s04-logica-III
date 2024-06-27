#Exercício de Casa 🏠 Grupo 2 - Atividade Fibonacci
##A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

while True:
    try:
        n = int(input("Informe o número de termos da série de Fibonacci que deseja gerar: "))
        if n >= 1:
            break
        else:
            print("Por favor, informe um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, informe um número inteiro.")
fibonacci = [1, 1]
    
if n > 2:
    for i in range(2, n):
        proximo_termo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_termo)

# Ajusta a lista de Fibonacci para o caso de n == 1
if n == 1:
    fibonacci = [1]

print(f"Série de Fibonacci com {n} termos:")
print(fibonacci)