#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

n = int(input("Digite o valor de n (maior que zero): "))
fibonacci_sequence = fibonacci(n)
print(f"Sequência de Fibonacci até o {n}º termo:")
print(fibonacci_sequence)