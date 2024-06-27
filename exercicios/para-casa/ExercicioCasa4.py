num = int(input("Informe o número para a tabuada de 1 a 10: "))

if 1 <= num <= 10:
    print(f"Tabuada de {num}:")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
else:
    print("Número inválido. Informe um número entre 1 e 10.")
