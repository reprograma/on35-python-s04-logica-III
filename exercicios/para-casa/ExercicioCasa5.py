n = int(input("Informe o valor de n: "))
a, b = 1, 1

print(f"Série de Fibonacci até a posição {n}:")
for _ in range(n):
    print(a)
    a, b = b, a + b
