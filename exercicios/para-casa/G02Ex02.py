# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

serie_fibonacci = []
contador = 0
n1 = 0
n2 = 1

for contador in range(15):
    print(contador)
    n1, n2 = n2, n1 + n2
    serie_fibonacci.append(n1)

sequencia = int(input(serie_fibonacci)) + 1
print(f"A sequência de fibonacci é {sequencia}")

