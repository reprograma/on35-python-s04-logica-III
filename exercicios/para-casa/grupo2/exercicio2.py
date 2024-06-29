#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibonacci(numero):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < numero_inserido:
        sequencia = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(sequencia)
    return fibonacci_sequence

numero_inserido = int(input("Digite o valor de n (maior que zero): "))
fibonacci_sequence = fibonacci(numero_inserido)
print(f"Sequência de Fibonacci até o {numero_inserido}º termo:")
print(fibonacci_sequence)