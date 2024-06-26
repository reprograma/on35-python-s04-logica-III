# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input("Quantos termos da sequência de Fibonacci deseja? "))

fibonacci = [1, 1]

if n <= 0:
    print("Número inválido!")
elif n == 1:
    print(fibonacci[0])
else:
    for contador in range(1, n-1):
        fibonacci.append(fibonacci[contador] + fibonacci[contador - 1])
    print(fibonacci)
