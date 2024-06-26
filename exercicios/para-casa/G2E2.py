# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Por favor, digite qual termo você deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    contagem=3
    while contagem <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        contagem += 1
    print(termo)