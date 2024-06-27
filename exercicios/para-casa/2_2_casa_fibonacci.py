# Exercício de Casa - Grupo 2🏠

# * A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def digite():

    num = int(input("Digite um número: "))
    resultado = fibonacci(num)
    return resultado    

def fibonacci(num):
    i = 1
    lista = [1,1]

    for i in range (1,num-1):
    
        x = lista[i-1] + lista[i]

        lista.append(x)   

        i = i + 1

    print(lista)

digite()


